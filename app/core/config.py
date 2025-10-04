from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    # App settings
    app_name: str = "DKMC Backend"
    debug: bool = False
    
    # Database settings
    database_url: str = "sqlite+aiosqlite:///./dkmc.db"
    
    # API settings
    api_v1_prefix: str = "/api/v1"
    
    # Security settings
    secret_key: str = "your-secret-key-here"
    access_token_expire_minutes: int = 30
    
    class Config:
        env_file = ".env"


settings = Settings()
