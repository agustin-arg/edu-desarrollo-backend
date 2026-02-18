#En el curso de fastapi lo hice con Pydantic Settings
from os import environ
from dotenv import load_dotenv

load_dotenv()


class Setting:
    DB_USER: str = environ.get("DB_USER")
    DB_PASSWORD: str = environ.get("DB_PASSWORD")
    DB_HOST: str = environ.get("DB_HOST")
    DB_PORT: int = environ.get("DB_PORT")
    DB_NAME: str = environ.get("DB_NAME")

    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


setting = Setting()
