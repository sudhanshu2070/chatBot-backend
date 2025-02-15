from fastapi import APIRouter, HTTPException
from app.models.example_model import ItemCreate, ItemResponse
from app.services.example_service import create_item, get_items

router = APIRouter()

@router.post("/items", response_model=ItemResponse, tags=["Items"])
async def create_new_item(item: ItemCreate):
    return await create_item(item)

@router.get("/items", response_model=list[ItemResponse], tags=["Items"])
async def list_items():
    return await get_items()