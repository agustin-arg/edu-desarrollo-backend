from typing import TYPE_CHECKING, List
from .base import (
    SQLModel,
    Field,
    Relationship,
    EmailStr,
    field_validator,
    Session,
    select,
)
from .plan import CustomerPlan
from db import SessionDep

if TYPE_CHECKING:
    from .transaction import Transaction
    from .plan import Plan


class CustomerBase(SQLModel):
    name: str = Field(default=None)
    description: str | None = Field(default=None)
    email: EmailStr = Field(default=None)
    age: int = Field(default=None)

    @field_validator("email")
    @classmethod
    def validate_email(selg, value):
        session = Session(SessionDep)
        query = select(Customer).where(Customer.email==value)
        result = session.exec(query).first()
        if result:
            raise ValueError("This email is already registered")
        return value


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
