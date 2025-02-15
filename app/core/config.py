from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str
    DEBUG: bool
    CHATPDF_API_KEY: str

    class Config:
        env_file = ".env"

settings = Settings()