from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/reset")
async def login_page(request: Request):
    return templates.TemplateResponse(
        "bases/auth-control/auth-control.html",
        {"request": request, "partial": "partials/reset-form/reset-form.html"},
    )

