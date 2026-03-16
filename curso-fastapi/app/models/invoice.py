from .base import BaseModel
from .customer import Customer
from .transaction import Transaction


class Invoice(BaseModel):
    id: int
    customer: Customer
    transactions: list[Transaction]
    total: int

    def calculate_total(self):
        return sum(transaction.ammount for transaction in self.transactions)
