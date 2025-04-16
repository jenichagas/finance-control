from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from app.utils.dependencies import get_current_user
from fastapi.responses import RedirectResponse


router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/dashboard")
async def dashboard(request: Request):
    user = await get_current_user(request)
    if not user:
        return RedirectResponse("/login")

    return templates.TemplateResponse("bases/main.html", {
        "request": request,
        "user_name": user["name"],
        "partial": "partials/home/dashboard.html"
    })
