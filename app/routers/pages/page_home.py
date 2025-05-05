from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from app.config.mongodb import db
from app.utils.serialize_category import serialize_category

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/")
async def home(request: Request):
    cursor = db.categories.find({})
    raw_categories = await cursor.to_list(length=None)
    category_list = [serialize_category(cat) for cat in raw_categories]

    return templates.TemplateResponse("bases/app/app.html", {
        "request": request,
        "partial": "partials/home/dashboard/dashboard.html",
        "categories": category_list
        
    })


