from fastapi import APIRouter
from models import Transaction

router = APIRouter(tags=["transactions"])

@router.post("/transaction", tags=['customers'])
async def create_transaction(customer_data: Transaction):
    return customer_data