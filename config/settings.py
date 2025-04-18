import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    load_dotenv()
    TG_BOT_TOKEN: str = os.environ.get("TG_BOT_TOKEN")


config = Settings()
