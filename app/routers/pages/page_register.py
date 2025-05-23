from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/register")
async def login_page(request: Request, error: str = None):
    return templates.TemplateResponse(
        "bases/auth-control/auth-control.html",
        {
            "request": request,
            "partial": "partials/register-form/register-form.html",
            "error": error,
        },
    )
