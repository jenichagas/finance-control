from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime, timezone


class User(BaseModel):
    name: str = Field(..., min_length=2, example="Jeniffer Chagas")
    email: EmailStr


class UserCreate(User):
    password: str = Field(..., min_length=6, example="senhaSegura123")


class UserInDB(User):
    hashed_password: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    is_active: bool = True
    role: Optional[str] = "user"


class UserOut(User):
    id: str
    created_at: datetime
    role: Optional[str]
