from pydantic import BaseModel, Field

class EchoRequest(BaseModel):
    message: str = Field(description="Text sent from Rails")
    source: str = Field(default="rails", description="Name of the app")

class EchoResponse(BaseModel):
    received: str = Field(description = "Hi Rails!")
    source: str
    processed_by: str=Field(default="AI- Microservice")