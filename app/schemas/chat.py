from pydantic import BaseModel, Field

class UserPrompt(BaseModel):
    prompt: str = Field(description="User Prmpt to AI")
    system: str = Field(
        default="You are a helpful AI assistant", 
        description="System instruction that set's the AI model behaviour"
    )

class AIResponse(BaseModel):
    reply: str = Field(description = "Hi Rails!")
    model: str=Field(default="AI- Microservice")