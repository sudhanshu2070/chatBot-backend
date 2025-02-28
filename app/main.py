from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # Import CORSMiddleware
from app.api.endpoints.chatpdf import router as chatpdf_router

app = FastAPI(
    title="FastAPI ChatPDF Integration",
    version="0.1.0",
    description="A FastAPI project integrated with ChatPDF."
)

# Allow frontend to make requests to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Include routers
app.include_router(chatpdf_router, prefix="/api/v1")

@app.get("/", tags=["Root"])
async def root():
    return {"message": "Welcome to the FastAPI ChatPDF Integration!"}