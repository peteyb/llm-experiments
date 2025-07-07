from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    host: str = "0.0.0.0"
    port: int = 8900
    reload: bool = True

    model_config = {"env_file": ".env", "case_sensitive": False}


settings = Settings()
