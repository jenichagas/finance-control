from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/")
async def home(request: Request):
    return templates.TemplateResponse("bases/main/main.html", {
        "request": request,
        "partial": "partials/home/home/home.html"
    })


