from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse
from app.utils.dependencies import get_current_user
from app.config.mongodb import db
from app.utils.security import hash_password
from bson import ObjectId

router = APIRouter()

@router.post("/meu-perfil")
async def update_profile(
    request: Request,
    name: str = Form(...),
    password: str = Form(None)
):
    user = await get_current_user(request)
    if not user:
        return RedirectResponse("/login", status_code=302)

    update_fields = {"name": name}
    if password:
        update_fields["hashed_password"] = hash_password(password)

    await db.users.update_one(
        {"_id": ObjectId(user["_id"])},
        {"$set": update_fields}
    )

    return RedirectResponse("/meus-dados?success=1", status_code=302)
