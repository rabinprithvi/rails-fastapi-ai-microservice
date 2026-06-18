# router file handle incoming request and describes which view it can render

# first import libraries used
from fastapi import APIRouter
from app.schemas.echo import EchoRequest, EchoResponse

router = APIRouter(prefix="/api/v1", tags=["EchoRails"])


@router.post("/echo", response_model=EchoResponse )
async def echo(payload: EchoRequest) -> EchoResponse:
    return EchoResponse(
        received=payload.message,
        source=payload.source,
    )