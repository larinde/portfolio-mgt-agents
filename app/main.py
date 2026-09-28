from fastapi import FastAPI
from .routers import chat_router
from .internal import lifespan

app = FastAPI(
    title="portfolio-mgt-agents", 
    description="An agentic workflow for monitoring and managing portfolios",
    version="0.1.0",
    lifespan=lifespan
)

# Include extra routers
app.include_router(chat_router, prefix="/chat")

# Set up healthcheck endpoint
@app.get("/")
async def healthcheck():
    """Healthcheck endpoint to verify API is running."""
    return {
        "title": app.title,
        "description": app.description,
        "version": app.version,
        "status": "OK"
    }
