# router file handle incoming request and describes which view it can render

# first import libraries used
from fastapi import APIRouter
from app.schemas.chat import UserPrompt, AIResponse 
from app.services.llm import get_chat

router = APIRouter(prefix="/api/v1", tags=["Completion"])


@router.post("/chat", response_model=AIResponse)
async def chat(payload: UserPrompt) -> AIResponse:
    result = await get_chat(payload.prompt, payload.system)
    return AIResponse( **result  )