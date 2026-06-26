# LangChain Memory Chain — Revision Notes
> Written by Rabin, corrected and enhanced for accuracy.

---

## The Complete Picture

```python
store = {}

def get_session_history(session_id: str) -> InMemoryChatMessageHistory:
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder(variable_name="history"),  # ← memory slot
    ("human", "{input}"),
])

llm = ChatGroq(model="llama-3.1-8b-instant", api_key=...)

chain = prompt | llm

chain_with_memory = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",
)

session = {"configurable": {"session_id": "user_123"}}

reply = chain_with_memory.invoke({"input": "My name is Rabin."}, config=session)
```

---

## Point-by-Point Explanation

### 1. `RunnableWithMessageHistory` — what it is

**Your understanding:** Like a Ruby Proc — a method assigned to a variable that can be invoked.

**Correction:** Close, but more precise:

It is a **wrapper object** (decorator pattern) that wraps your existing chain and adds memory behaviour to it. Every time you call `.invoke()` on it, it automatically:
1. Fetches the session history
2. Injects it into the prompt
3. Runs the inner chain
4. Saves the new messages back to history

Ruby analogy: like a `before_action` + `after_action` pair wrapped around a controller method — the original method is unchanged, the wrapper adds behaviour around it.

---

### 2. Invoking with two parameters

**Your understanding:** Correct.

```python
chain_with_memory.invoke(
    {"input": "My name is Rabin."},              # param 1 — user input dict
    config={"configurable": {"session_id": "user_123"}}  # param 2 — session dict
)
```

- Param 1: the current user's message — same as any chain invoke
- Param 2: runtime config — tells LangChain which session to load history for

---

### 3. What is `session` / `configurable`

**Your understanding:** Correct.

```python
session = {"configurable": {"session_id": "user_123"}}
```

- `"configurable"` is a **hardcoded LangChain key** — not a Python keyword, not flexible
- LangChain looks inside `config["configurable"]` to find runtime settings
- `"session_id"` is the key your `get_session_history` function receives as its argument

Rails analogy: like `params` — a standard envelope for request-level context.

---

### 4. `RunnableWithMessageHistory` constructor parameters

**Your understanding:** Partially correct — the Proc analogy works but the parameter names need clarification.

```python
chain_with_memory = RunnableWithMessageHistory(
    chain,                          # the chain to wrap
    get_session_history,            # function to fetch history by session_id
    input_messages_key="input",     # which key in your invoke dict is the user message
    history_messages_key="history", # which variable_name in MessagesPlaceholder to fill
)
```

- `input_messages_key="input"` — tells LangChain that `{"input": "..."}` is the human message
- `history_messages_key="history"` — tells LangChain to fill `MessagesPlaceholder(variable_name="history")` with past messages

**The three names must match:**
```
invoke({"input": ...})                       ← input_messages_key="input"
MessagesPlaceholder(variable_name="history") ← history_messages_key="history"
```

---

### 5. The `store` and `InMemoryChatMessageHistory`

**Your understanding:** Correct.

```python
store = {
    "user_123": InMemoryChatMessageHistory(messages=[
        HumanMessage("My name is Rabin."),
        AIMessage("Nice to meet you, Rabin!"),
        HumanMessage("I work as a Ruby engineer."),
        AIMessage("That's great experience!"),
    ]),
    "user_456": InMemoryChatMessageHistory(messages=[...]),
}
```

- `store` is a plain Python dict — lives in process memory, wiped on server restart
- Each value is one `InMemoryChatMessageHistory` object per user
- `get_session_history` creates a new one on first call, returns the existing one on every subsequent call
- LangChain appends new messages to the object automatically after each turn

**Production note:** Replace `store = {}` with Redis for persistence across restarts.

---

### 6. `chain = prompt | llm`

**Your understanding:** Unsure what object it is.

**Answer:** It is a `RunnableSequence` object — LangChain's internal type for a pipeline of steps connected by `|`.

```python
chain = prompt | llm
# chain is now a RunnableSequence:
# Step 1: prompt.invoke(input) → formats the messages
# Step 2: llm.invoke(formatted_messages) → returns AIMessage
```

You never instantiate `RunnableSequence` directly. The `|` operator creates it automatically. When you call `chain.invoke(...)`, it runs each step left to right.

---

### 7. `ChatPromptTemplate` and `MessagesPlaceholder`

**Your understanding:** Mostly correct — good instinct on the variable name matching.

```python
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),  # fixed context for LLM behaviour
    MessagesPlaceholder(variable_name="history"), # dynamic slot — filled with past messages
    ("human", "{input}"),                         # current user message
])
```

- `ChatPromptTemplate.from_messages([...])` — creates a template from a list of message tuples
- `MessagesPlaceholder(variable_name="history")` — reserves a slot where a **list of messages** will be injected at runtime
- The `variable_name="history"` must match `history_messages_key="history"` in `RunnableWithMessageHistory`

**Key distinction:** `{input}` is a single string variable. `MessagesPlaceholder` injects a **list of full message objects** — not a string. That is why they use different syntax.

---

### 8. `llm = ChatGroq(...)`

**Your understanding:** Correct — you know this one.

```python
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY"),
)
```

The LLM object. Swappable — replace `ChatGroq` with `ChatOpenAI` or `ChatAnthropic` and the rest of the code is unchanged.

---

## The Matching Rules — Most Important

Three names must be consistent across your code:

| Where | Name | Must match |
|-------|------|-----------|
| `invoke({"input": ...})` | `"input"` | `input_messages_key="input"` |
| `MessagesPlaceholder(variable_name="history")` | `"history"` | `history_messages_key="history"` |
| `get_session_history(session_id)` | function name | second argument to `RunnableWithMessageHistory` |

---

## What happens on every `.invoke()` call

```
chain_with_memory.invoke({"input": "What's my name?"}, config=session)

1. Reads session_id from config["configurable"]["session_id"]
2. Calls get_session_history("user_123") → returns store["user_123"]
3. Injects store["user_123"].messages into MessagesPlaceholder("history")
4. Formats the full prompt: system + history + current input
5. Sends to LLM → gets AIMessage reply
6. Appends HumanMessage("What's my name?") + AIMessage(reply) to store["user_123"]
7. Returns AIMessage
```
