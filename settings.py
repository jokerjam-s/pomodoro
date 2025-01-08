from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    google_token_id: str = 'sfsdfsdfsfsdfsdfsdfsd'


settings = Settings()