from typing import TYPE_CHECKING, List
from .base import SQLModel, Field, Relationship
from .plan import CustomerPlan

if TYPE_CHECKING:
    from .transaction import Transaction
    from .plan import Plan

class CustomerBase(SQLModel):
    name: str = Field(default=None)
    description: str | None = Field(default=None)
    email: str = Field(default=None)
    age: int = Field(default=None)

class Customer(CustomerBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    transactions: List["Transaction"] = Relationship(back_populates="customer")
    plans: List["Plan"] = Relationship(
        back_populates="customers", link_model=CustomerPlan
    )

class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(CustomerBase):
    pass
