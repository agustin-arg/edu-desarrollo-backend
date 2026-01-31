import zoneinfo
from fastapi import FastAPI, HTTPException, status
from datetime import datetime
from models import Customer, CustomerCreate, Transaction, Invoice
from db import create_all_tables, SessionDep
from sqlmodel import select
      
app = FastAPI(lifespan=create_all_tables)


@app.get("/")
async def root():
    return{"message": "Hola yo!"}

country_timezones = {
    "CO": "America/Bogota",
    "MX": "America/Mexico_City",
    "AR": "America/Argentina/Buenos_Aires",
    "BR": "America/Sao_Paulo",
    "PE": "America/Lima",
}

@app.get("/time/{iso_code}", tags=['date'])
async def time(iso_code: str):
    iso = iso_code.upper()
    timezone_str = country_timezones.get(iso)
    tz = zoneinfo.ZoneInfo(timezone_str)
    return{"time": datetime.now(tz)}

@app.post("/customers", response_model= Customer, tags=['customers'])
async def create_customer(customer_data: CustomerCreate, session: SessionDep):
    customer = Customer.model_validate(customer_data.model_dump())
    session.add(customer)
    session.commit() #Siempre debe haber un commit
    session.refresh(customer)
    return customer 

@app.get("/customers", response_model=list[Customer], tags=['customers'])
async def list_customer(session: SessionDep):
    return session.exec(select(Customer)).all()

@app.post("/invoice", tags=['customers'])
async def create_invoice(customer_data: Invoice):
    return customer_data

@app.post("/transaction", tags=['customers'])
async def create_transaction(customer_data: Transaction):
    return customer_data

@app.post("/customers/{customer_id}", tags=['customers'])
async def get_customer(customer_id: int, session: SessionDep):
    if session.get(Customer, customer_id) == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found")
    return session.get(Customer, customer_id)