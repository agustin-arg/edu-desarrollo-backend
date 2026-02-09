from fastapi import FastAPI, Depends
from typing import Annotated
from sqlmodel import Session, create_engine, SQLModel
from config import settings

url_connection = settings.DATABASE_URL


engine = create_engine(url_connection)


def create_all_tables(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
