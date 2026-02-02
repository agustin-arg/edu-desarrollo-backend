from fastapi import APIRouter
from models import Invoice

router = APIRouter(tags=["invoices"])

@router.post("/invoice", tags=['customers'])
async def create_invoice(customer_data: Invoice):
    return customer_data
