from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from app.utils.dependencies import get_current_user
from fastapi.responses import RedirectResponse
from app.routers.debt_categories import CATEGORIES

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/dashboard")
async def dashboard(request: Request):
    return templates.TemplateResponse("bases/main/main.html", {
        "request": request,
        "partial": "partials/home/dashboard/dashboard.html",
        "categories": CATEGORIES
    })
