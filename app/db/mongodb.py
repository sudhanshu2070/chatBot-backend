from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

# MongoDB client
client = AsyncIOMotorClient(settings.MONGODB_URL)

# Database instance
db = client[settings.MONGODB_DB_NAME]