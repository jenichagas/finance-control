from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/login")
async def login_page(request: Request, success: bool = False):
    return templates.TemplateResponse(
        "bases/auth-control/auth-control.html",
        {"request": request, "partial": "partials/login-form/login-form.html", "success": success},
    )

