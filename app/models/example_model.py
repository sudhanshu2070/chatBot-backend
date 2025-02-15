from pydantic import BaseModel

class ItemCreate(BaseModel):
    name: str
    description: str

class ItemResponse(BaseModel):
    id: str
    name: str
    description: str