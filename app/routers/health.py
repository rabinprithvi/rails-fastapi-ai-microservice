from fastapi import APIRouter
from app.schemas.health import HealthResponse

router = APIRouter(prefix="/api/v1", tags=["Health"])


@router.get(
    "/health",
    response_model=HealthResponse,
    summary="Service liveness probe",
    description="Called by Rails (and load balancers) to confirm the AI microservice is alive.",
)
async def health_check() -> HealthResponse:
    return HealthResponse()
