from fastapi import FastAPI
from datetime import datetime


app = FastAPI()

@app.get("/")
async def root():
    return{"message": "Hola, mundo!"}