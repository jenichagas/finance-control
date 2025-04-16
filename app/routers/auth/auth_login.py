from fastapi import APIRouter, Form, Request, Response, HTTPException
from fastapi.responses import RedirectResponse
from app.utils.security import verify_password, create_access_token
from app.config.mongodb import db

router = APIRouter()

@router.post("/login")
async def login(
    response: Response,
    email: str = Form(...),
    password: str = Form(...)
):
    user = await db.users.find_one({"email": email})
    if not user or not verify_password(password, user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    token = create_access_token({"sub": str(user["_id"]), "name": user["name"]})
    response.set_cookie("session_token", token, httponly=True, max_age=60 * 60 * 24 * 7)
    return {"msg": "Login realizado com sucesso"}

@router.get("/logout")
def logout(response: Response):
    response.delete_cookie("session_token")
    return RedirectResponse("/login", status_code=302)