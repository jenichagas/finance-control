from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from starlette.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/configuracoes", response_class=HTMLResponse)
async def configuracoes_page(request: Request):
    return templates.TemplateResponse("partials/home/ajusts/ajusts.html", {"request": request})
