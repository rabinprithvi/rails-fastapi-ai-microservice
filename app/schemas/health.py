from datetime import datetime, timezone
from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    """Typed JSON contract for the /health endpoint — consumed by Rails and load balancers."""

    status: str = Field(default="ok", description="Service liveness status.")
    service: str = Field(default="ai-microservice", description="Name of this service.")
    version: str = Field(default="0.1.0", description="Current API version.")
    timestamp: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="UTC timestamp of this response.",
    )

    model_config = {
        "json_schema_extra": {
            "example": {
                "status": "ok",
                "service": "ai-microservice",
                "version": "0.1.0",
            }
        }
    }
