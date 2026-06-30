# request object -> service object -> response -> response object

#define request format and response object

from fastapi import APIRouter

from app.schemas.conversation import ConversationRequest, ConversationResponse
from app.services.conversation import get_conversation_reply


router = APIRouter(prefix="/api/v1", tags=["Conversation"])

@router.post("/conversation",response_model=ConversationResponse)
async def conversation(payload:ConversationRequest) -> ConversationResponse:
    result = await get_conversation_reply(
        payload.message,
        payload.session_id,
        payload.system,
    )
    return ConversationResponse(**result)

