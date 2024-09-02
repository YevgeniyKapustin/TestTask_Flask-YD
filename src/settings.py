from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Конфигурация приложения."""

    # APP
    APP_NAME: str
    SECRET_KEY: str

    class Config:
        env_file = '../.env', '../.flaskenv'
        env_file_encoding = 'utf-8'


settings = Settings()
