from pydantic import BaseModel
from pydantic import Field


class ConversationRequest(BaseModel):
  session_id: str = Field(description="User session from Rails")
  message: str = Field(description="User chat input")
  system: str = Field(
    default="You are helpful assistant.", 
    description="System instruction"
)  


class ConversationResponse(BaseModel):
    reply :str = Field(description="AI response")
    session_id :str = Field(description="Session id echoed back to Rails"
)

