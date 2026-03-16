from fastapi import APIRouter, HTTPException, Query, status
from app.models import Transaction, TransactionCreate, Customer
from db import SessionDep
from sqlmodel import select, func
from math import ceil

router = APIRouter(tags=["transactions"])


@router.post("/transaction")
async def create_transaction(transaction_data: TransactionCreate, session: SessionDep):
    transaction_data_dic = transaction_data.model_dump()
    customer = session.get(Customer, transaction_data_dic.get("customer_id"))
    if not customer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Customer not exist"
        )
    transaction_db = Transaction.model_validate(transaction_data_dic)
    session.add(transaction_db)
    session.commit()
    session.refresh(transaction_db)
    return transaction_db


@router.get("/transactions")
async def list_transaction(
    session: SessionDep,
    skip: int = Query(0, description="Registros a omitir"),
    limit: int = Query(10, description="Número de registros"),
):
    query1 = select(Transaction).offset(skip).limit(limit)
    transactions = session.exec(query1).all()
    
    query2 = select(func.count()).select_from(Transaction)
    count = session.exec(query2).one()
    
    pages = ceil(count / limit) if limit > 0 else 0
    
    return {
        "count": count,
        "pages": pages,
        "transactions": transactions
    }
