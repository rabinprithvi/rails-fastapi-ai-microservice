# define llm 
# define propmpt
# define parser
# define chain
# invoke chain
# print resul
# 
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
import os


prompt = ChatPromptTemplate.from_messages([
    ("system", "{system}"),
    ("human", "{question}"),
])

load_dotenv()

llm = ChatGroq( 
    model = "llama-3.1-8b-instant",
    api_key = os.getenv("GROQ_API_KEY")
)

parser = StrOutputParser()

chain = prompt | llm | parser

result = chain.invoke({
    "system": "You are Senior python Engineer. Be concise",
    "question": "What is LangChain in one sentence.",
})

print ("Reply: ", result)