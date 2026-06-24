import os
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

#define openAI client, model

load_dotenv()



MODEL = "llama-3.1-8b-instant"

prompt_template = ChatPromptTemplate([
    ("system", "{system}"),
     ("human", "{human}")
])

llm = ChatGroq(
    model=MODEL, 
    api_key= os.getenv("GROQ_API_KEY")
    )

chain = prompt_template | llm | StrOutputParser()



async def get_chat(prompt:str, system: str) -> dict:
    reply = await chain.ainvoke({"system": system, "human": prompt})
    return {
        "reply": reply,
        "model": MODEL,
    }