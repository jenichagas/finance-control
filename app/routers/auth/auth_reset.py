from fastapi import APIRouter, Form, HTTPException
from app.config.mongodb import db
from app.utils.security import hash_password
from app.utils.email import send_email
from app.utils.email_templates import password_reset_html  # caso separado

router = APIRouter()


@router.post("/reset-password")
async def reset_password(email: str = Form(...), new_password: str = Form(...)):
    user = await db.users.find_one({"email": email})
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    hashed_pw = hash_password(new_password)

    await db.users.update_one(
        {"_id": user["_id"]}, {"$set": {"hashed_password": hashed_pw}}
    )

    await send_email(
        to_email=email,
        subject="Sua senha foi redefinida",
        html_body=password_reset_html(user["name"]),
    )

    return {"msg": "Senha redefinida com sucesso"}
