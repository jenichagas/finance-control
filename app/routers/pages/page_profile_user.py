from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from app.utils.dependencies import get_current_user

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/meu-perfil", response_class=HTMLResponse)
async def profile_page(request: Request):
    
    return templates.TemplateResponse(
        "partials/home/profile-user/profile-user.html",
        {"request": request}
    )
