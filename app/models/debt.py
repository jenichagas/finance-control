from pydantic import BaseModel
from datetime import date
from typing import Optional


class Debt(BaseModel):
    name: str
    value: float
    category: str
    start_date: date
    installments: Optional [int] = 1
