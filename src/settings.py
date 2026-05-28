from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    database_url: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/auth_db"
    jwt_secret: str = "7f3c9a2d5e8b4c6f9a1d0e3b6c8f2a9d4e7b1c5f8a0d2e6c9b3f7a1d5e8c0b2"
    jwt_algorithm: str = "HS256"
    jwt_expire_hours: int = 24
    jwt_refresh_expire_days: int = 30
