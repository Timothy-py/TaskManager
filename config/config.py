from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DB_URI: str
    REDIS_HOST: str
    REDIS_PORT: int

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()

# Cache settings to improve performance
@lru_cache
def get_settings():
    return settings

env_vars = get_settings()