import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_groq import ChatGroq

load_dotenv()

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are helpful assistant. Remember the user tells you." ),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}"),
])


llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY"),
)

chain = prompt | llm

store = {}

def get_session_history(session_id: str) -> InMemoryChatMessageHistory:
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]


chain_with_memory = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",
)

session = {"configurable": {"session_id": "user_123"}}

turn1 = chain_with_memory.invoke({"input": "My name is Rabin."}, config=session)
print("Turn 1:", turn1.content)

turn2 = chain_with_memory.invoke({"input": "I work as a senior Ruby engineer."}, config=session)
print("Turn 2:", turn2.content)

turn3 = chain_with_memory.invoke({"input": "What do you know about me so far?"}, config=session)
print("Turn 3:", turn3.content)