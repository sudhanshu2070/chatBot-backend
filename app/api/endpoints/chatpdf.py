from fastapi import APIRouter, File, UploadFile, HTTPException, Depends
from fastapi.responses import JSONResponse
import requests
from app.core.config import settings

router = APIRouter()

# ChatPDF API base URL
CHATPDF_API_URL = "https://api.chatpdf.com/v1"

# Headers for ChatPDF API
headers = {
    "x-api-key": settings.CHATPDF_API_KEY,
    "Content-Type": "application/json",
}

# Store the source ID of the uploaded PDF
source_id = None

@router.post("/upload-pdf", tags=["ChatPDF"])
async def upload_pdf(file: UploadFile = File(...)):
    """
    Upload a PDF file to ChatPDF and store its source ID.
    """
    global source_id

    # Check if the file is a PDF
    if not file.content_type == "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are allowed.")

    # Prepare the file for upload
    files = {"file": (file.filename, file.file, file.content_type)}
    response = requests.post(
        f"{CHATPDF_API_URL}/sources/add-file",
        headers={"x-api-key": settings.CHATPDF_API_KEY},
        files=files,
    )

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())

    # Extract the source ID from the response
    source_id = response.json().get("sourceId")
    return {"message": "PDF uploaded successfully.", "sourceId": source_id}


@router.post("/query-pdf", tags=["ChatPDF"])
async def query_pdf(question: dict):
    """
    Ask a question about the uploaded PDF and get a response.
    """
    global source_id

    if not source_id:
        raise HTTPException(status_code=400, detail="No PDF has been uploaded yet.")

    # Prepare the query payload
    payload = {
        "sourceId": source_id,
        "messages": [
            {
                "role": "user",
                "content": question.get("question"),
            }
        ],
    }

    # Print URL and headers for debugging
    print(f"URL: {CHATPDF_API_URL}/chat")
    print(f"Headers: {headers}")
    print(f"Payload: {payload}")

    # Send the query to ChatPDF
    response = requests.post(
        f"{CHATPDF_API_URL}/chat",
        headers=headers,
        json=payload,
    )

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())

    # Extract the response content
    answer = response.json().get("content")
    return {"answer": answer}