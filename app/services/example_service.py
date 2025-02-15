from app.db.mongodb import db
from app.models.example_model import ItemCreate

async def create_item(item_data: ItemCreate):
    result = await db["items"].insert_one(item_data.dict())
    return {"id": str(result.inserted_id), **item_data.dict()}

async def get_items():
    items = []
    async for item in db["items"].find():
        items.append({"id": str(item["_id"]), **item})
    return items