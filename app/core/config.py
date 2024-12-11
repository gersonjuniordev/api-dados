from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    REDIS_URL: str = "redis://localhost:6379"
    CACHE_EXPIRATION: int = 3600
    
    class Config:
        env_file = ".env"

settings = Settings() 