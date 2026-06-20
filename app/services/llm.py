import asyncio
import os
from dotenv import load_dotenv
from openai import OpenAI

#define openAI client, model

load_dotenv()

client = OpenAI(
    #key and URL
    api_key = os.getenv("GROQ_API_KEY"),
    base_url = "https://api.groq.com/openai/v1",
)

MODEL = "llama-3.1-8b-instant"

async def get_chat(prompt:str, system: str) -> dict:
    llm_response = await asyncio.to_thread(
        client.chat.completions.create,
        model = MODEL,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": prompt},
        ],
    )
    return{
        "reply": llm_response.choices[0].message.content,
        "model": llm_response.model,
    }