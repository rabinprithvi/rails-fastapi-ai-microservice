from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.routers import health
from app.routers import chat


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup — runs before the first request.
    # Future: connect ChromaDB, load ML models, warm caches here.
    print("AI microservice starting up...")
    yield
    # Shutdown — runs after the last request is handled.
    print("AI microservice shutting down.")


app = FastAPI(
    title="Rails-FastAPI AI Microservice",
    description="Asynchronous Python AI engine consumed by a Ruby on Rails backend.",
    version="0.1.0",
    lifespan=lifespan,
)

app.include_router(health.router)
app.include_router(chat.router)
