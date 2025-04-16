from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.responses import RedirectResponse
from app.models.user import UserCreate, UserInDB
from app.config.mongodb import db
from app.utils.security import hash_password
from datetime import datetime, timezone

router = APIRouter()

@router.post("/register")
async def register(
    name: str = Form(...),
    email: str = Form(...),
    password: str = Form(...)
):
    existing_user = await db.users.find_one({"email": email})
    if existing_user:
        raise HTTPException(status_code=400, detail="E-mail já registrado.")

    hashed_pw = hash_password(password)

    user = UserInDB(
        name=name,
        email=email,
        hashed_password=hashed_pw,
        created_at=datetime.now(timezone.utc),
        is_active=True,
        role="user"
    )

    result = await db.users.insert_one(user.model_dump())
    return RedirectResponse("/login", status_code=302)