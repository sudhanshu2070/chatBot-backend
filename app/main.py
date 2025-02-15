from fastapi import FastAPI
from app.api.endpoints.chatpdf import router as chatpdf_router

app = FastAPI(
    title="FastAPI ChatPDF Integration",
    version="0.1.0",
    description="A FastAPI project integrated with ChatPDF."
)

# Include routers
app.include_router(chatpdf_router, prefix="/api/v1")

@app.get("/", tags=["Root"])
async def root():
    return {"message": "Welcome to the FastAPI ChatPDF Integration!"}