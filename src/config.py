# file purpose: uses pydantic-settings to read .env file and validate the values
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    model_config = SettingsConfigDict(
        env_file = ".env",
        env_file_encoding="utf-8",
        # ignores extra variables in .env that aren't defined in this class
        extra = "ignore"
    )
