from enum import Enum
from typing import TYPE_CHECKING, List
from .base import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .customer import Customer


class StatusEnum(str, Enum):
    ACTIVE = "activate"
    INACTIVE = "inactive"


class CustomerPlan(SQLModel, table=True):
    id: int = Field(primary_key=True)
    plan_id: int = Field(foreign_key="plan.id")
    customer_id: int = Field(foreign_key="customer.id")


class PlanBase(SQLModel):
    name: str = Field(default=None)
    price: float = Field(default=None)
    descripcion: str = Field(default=None)


class Plan(PlanBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    customers: List["Customer"] = Relationship(
        back_populates="plans", link_model=CustomerPlan
    )


class PlanCreate(PlanBase):
    pass
