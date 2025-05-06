from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from starlette.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/carteira", response_class=HTMLResponse)
async def show_wallet(request: Request):
    # Aqui futuramente você pode buscar dados do banco
    return templates.TemplateResponse("partials/home/wallet/wallet.html", {
        "request": request,
    })
