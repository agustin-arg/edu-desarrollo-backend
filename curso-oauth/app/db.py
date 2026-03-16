from fastapi import FastAPI, Depends
from typing import Annotated
from sqlmodel import Session, create_engine, SQLModel



engine = create_engine(f"sqlite:///users.db")


def create_all_tables(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
