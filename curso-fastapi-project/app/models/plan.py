from typing import TYPE_CHECKING, List
from .base import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .customer import Customer

class CustomerPlan(SQLModel, table=True):
    id: int = Field(primary_key=True)
    plan_id: int = Field(foreign_key="plan.id")
    customer_id: int = Field(foreign_key="customer.id")

class Plan(SQLModel, table=True):
    id: int | None = Field(primary_key=True)
    name: str = Field(default=None)
    price: float = Field(default=None)
    descripcion: str = Field(default=None)
    customers: List["Customer"] = Relationship(
        back_populates="plans", link_model=CustomerPlan
    )
