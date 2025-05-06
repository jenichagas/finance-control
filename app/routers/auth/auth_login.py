from fastapi import APIRouter, Form, Request, Response, HTTPException
from fastapi.responses import RedirectResponse
from app.utils.security import verify_password, create_access_token
from fastapi.responses import HTMLResponse
from app.config.mongodb import db
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.post("/login", response_class=HTMLResponse)
async def login(
    request: Request,
    response: Response,
    email: str = Form(...),
    password: str = Form(...),
):
    user = await db.users.find_one({"email": email})
    if not user or not verify_password(password, user["hashed_password"]):
        return templates.TemplateResponse(
            "bases/auth-control/auth-control.html",
            {
                "request": request,
                "partial": "partials/login-form/login-form.html",
                "error": "E-mail ou senha inválidos",
            },
            status_code=401,
        )

    token = create_access_token({"sub": str(user["_id"]), "name": user["name"]})
    response.set_cookie("session_token", token, httponly=True, max_age=60 * 60 * 24 * 7)
    return HTMLResponse(status_code=200, headers={"HX-Redirect": "/"})


@router.get("/logout")
def logout(response: Response):
    response.delete_cookie("session_token")
    return RedirectResponse("/login", status_code=302)
