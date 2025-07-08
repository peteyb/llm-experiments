from pydantic_settings import BaseSettings
from uvicorn.config import LifespanType


class Settings(BaseSettings):
    host: str = "0.0.0.0"
    port: int = 8900
    reload: bool = True
    lifespan: LifespanType = "on"

    model_config = {"env_file": ".env", "case_sensitive": False}


settings = Settings()
