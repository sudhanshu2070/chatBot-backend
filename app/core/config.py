from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI MongoDB Boilerplate"
    DEBUG: bool = True
    MONGODB_URL: str = "mongodb://localhost:27017"  # MongoDB connection URL
    MONGODB_DB_NAME: str = "my_fastapi_db"          # Database name

    class Config:
        env_file = ".env"

settings = Settings()