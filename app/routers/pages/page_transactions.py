from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/transacoes")
async def transaction_page(request: Request):
    return templates.TemplateResponse(
        "partials/home/transactions/transactions.html", 
        {
            "request": request
        }
    )
