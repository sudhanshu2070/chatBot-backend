from fastapi import FastAPI
from app.api.endpoints.example import router as example_router
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version="0.1.0",
    description="A FastAPI + MongoDB Boilerplate Project"
)

# Include routers
app.include_router(example_router, prefix="/api/v1")

@app.get("/", tags=["Root"])
async def root():
    return {"message": "Welcome to the FastAPI + MongoDB Boilerplate!"}