from pydantic import BaseModel
from typing import List

#define nested models
class User(BaseModel):
    name: str
    email: str

class Purchase(BaseModel):
    product: str
    price: float

class Record(BaseModel):
    id: int
    user: User
    purchases: List[Purchase]

# Sample JSON input
json_data = '''
{
  "id": 101,
  "user": {
    "name": "Alice",
    "email": "alice@example.com"
  },
  "purchases": [
    {"product": "A", "price": 9.99},
    {"product": "B", "price": 14.99}
  ]
}
'''

# Parse Json data using pydantic
record = Record.model_validate_json(json_data)

#extract data
print(f"User: {record.user.name}, Email: {record.user.email}")
total_spend = sum(p.price for p in record.purchases)
print(f"Total Spend: ${total_spend:.2f}")