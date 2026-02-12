from fastapi import APIRouter, status, HTTPException, Query
from sqlmodel import select

from app.models import (
    Customer,
    CustomerCreate,
    CustomerUpdate,
    Plan,
    CustomerPlan,
    StatusEnum,
)
from db import SessionDep

router = APIRouter(prefix="/customers", tags=["customers"])


@router.post("/", response_model=Customer, status_code=status.HTTP_201_CREATED)
async def create_customer(customer_data: CustomerCreate, session: SessionDep):
    customer = Customer.model_validate(customer_data.model_dump())
    session.add(customer)
    session.commit()
    session.refresh(customer)
    return customer


@router.get("/{customer_id}", response_model=Customer)
async def get_customer(customer_id: int, session: SessionDep):
    customer = session.get(Customer, customer_id)
    if customer is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found"
        )
    return customer


@router.get("/", response_model=list[Customer])
async def list_customers(session: SessionDep):
    return session.exec(select(Customer)).all()


@router.patch("/{customer_id}", response_model=Customer)
async def update_customer(
    customer_id: int, customer_data: CustomerUpdate, session: SessionDep
):
    customer_db = session.get(Customer, customer_id)
    if customer_db is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found"
        )
    customer_data_dict = customer_data.model_dump(exclude_unset=True)
    customer_db.sqlmodel_update(customer_data_dict)
    session.add(customer_db)
    session.commit()
    session.refresh(customer_db)
    return customer_db


@router.delete("/{customer_id}")
async def delete_customer(customer_id: int, session: SessionDep):
    customer_db = session.get(Customer, customer_id)
    if customer_db is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found"
        )
    session.delete(customer_db)
    session.commit()
    return {"detail": "Customer deleted successfully"}


@router.post("/{customer_id}/plans/{plan_id}", tags=["plans"])
async def subscribe_custmer_to_plan(
    customer_id: int,
    plan_id: int,
    session: SessionDep,
    plan_status: StatusEnum = Query(),
):
    customer_db = session.get(Customer, customer_id)
    plan_db = session.get(Plan, plan_id)
    if customer_db is None or plan_db is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Customer or plan not found"
        )
    customer_plan_db = CustomerPlan(
        customer_id=customer_id, plan_id=plan_id, status=plan_status
    )
    session.add(customer_plan_db)
    session.commit()
    session.refresh(customer_plan_db)
    return customer_plan_db


@router.get("/{customer_id}/plans", tags=["plans"])
async def list_plans_customer(
    customer_id: int, session: SessionDep, plan_status: StatusEnum = Query()
):
    customer_db = session.get(Customer, customer_id)
    if customer_db is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found"
        )
    query = (
        select(CustomerPlan)
        .where(CustomerPlan.customer_id == customer_id)
        .where(CustomerPlan.status == plan_status)
    )
    plans = session.exec(query).all()
    return plans
