from pydantic import BaseModel
from datetime import date
from typing import Optional


class DebtUpdate(BaseModel):
    name: Optional [str] = None
    value: Optional [float] = None
    category: Optional [str] = None
    start_date: Optional [date] = None
    installments: Optional [int] = None
