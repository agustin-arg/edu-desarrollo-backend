from fastapi import APIRouter
from models import Plan, PlanCreate
from db import SessionDep
from sqlmodel import select

router = APIRouter(prefix="/plans" ,tags=["plans"])

@router.post("/", response_model=Plan)
async def create_plan(plan_data: PlanCreate, session: SessionDep):
    plan_db = Plan.model_validate(plan_data.model_dump())
    session.add(plan_db)
    session.commit()
    session.refresh(plan_db)
    return plan_db
 
@router.get("/", response_model=list[Plan])
async def list_plans(session: SessionDep): 
    return session.exec(select(Plan)).all()