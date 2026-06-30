import os
from dotenv import load_dotenv
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_groq.chat_models import ChatGroq



load_dotenv()

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "{system}"),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}"),
    ]
)

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

async def get_conversation_reply(message: str, session_id: str, system: str) -> dict:
    config =  {"configurable": {"session_id": session_id}}
    reply = await chain_with_memory.ainvoke(
        {"input": message, "system": system},
        config=config,
    )
    return {
        "reply": reply.content,
        "session_id": session_id
    }
   

