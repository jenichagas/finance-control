from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from app.utils.dependencies import get_current_user

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/meu-perfil")
async def profile_page(request: Request, success: bool = False):
    user = await get_current_user(request)
    if not user:
        return RedirectResponse("/login", status_code=302)
    
    return templates.TemplateResponse(
        "bases/main/main.html",
        {
            "request": request,
            "partial": "partials/profile-user/profile-user.html",
            "user": user,
            "success": success,
        },
    )
