from pydantic import BaseModel, Field

class UserPrompt(BaseModel):
    prompt: str = Field(description="The user's question or instruction sent from Rails..")
    system: str = Field(
        default="You are a helpful AI assistant",
        description="System instruction that sets the AI model behaviour.",
    )


class AIResponse(BaseModel):
    reply: str = Field(description="The LLM's generated response.")
    model: str = Field(description="The model that generated the reply.")