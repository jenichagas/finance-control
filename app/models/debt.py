from pydantic import BaseModel
from datetime import date


class Debt(BaseModel):
    name: str
    value: float
    category: str
    start_date: date
    installments: int = 1
