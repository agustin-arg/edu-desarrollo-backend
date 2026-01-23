from pydantic import BaseModel 

class CustomerBase(BaseModel):
    name: str
    description: str
    email: str
    age: int
    
class Customer(CustomerBase):
    id: int | None = None
    
class CustomerCreate(CustomerBase):
    pass
    
class Transaction(BaseModel):
    id: int
    ammount: int
    description: str

class Invoice(BaseModel):
    id: int
    customer: Customer
    transactions: list[Transaction]
    total: int
    
    def total(self):
        return sum(transactions.ammount for transaction in self.transactions)
    