import zoneinfo
from fastapi import FastAPI
from datetime import datetime
from models import Customer, CustomerCreate, Transaction, Invoice    
      
app = FastAPI()

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

@app.get("/time/{iso_code}")
async def time(iso_code: str):
    iso = iso_code.upper()
    timezone_str = country_timezones.get(iso)
    tz = zoneinfo.ZoneInfo(timezone_str)
    return{"time": datetime.now(tz)}


db_customer: list[Customer] = []

@app.post("/customers", response_model= Customer)
async def create_customer(customer_data: CustomerCreate):
    customer = Customer.model_validate(customer_data.model_dump())
    customer.id = len(db_customer)
    db_customer.append(customer)
    return customer 

@app.get("/customers", response_model=list[Customer])
async def list_customer():
    return db_customer

@app.post("/invoice")
async def create_invoice(customer_data: Invoice):
    return customer_data

@app.post("/transaction")
async def create_transaction(customer_data: Transaction):
    return customer_data