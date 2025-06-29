from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str = "postgresql://postgres:postgres@localhost:5432/book_review_db"
    redis_url: str = "redis://localhost:6379"
    cache_expiration: int = 300  # 5 minutes

    class Config:
        env_file = ".env"

settings = Settings()