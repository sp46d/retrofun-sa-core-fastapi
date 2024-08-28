from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    user_name: str
    password: str
    host: str
    port: int
    database: str


settings = Settings()