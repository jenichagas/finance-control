from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from app.utils.dependencies import get_current_user
from app.config.mongodb import db
from app.utils.serialize_category import serialize_category


router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/dashboard")
async def dashboard(request: Request):
    cursor = db.categories.find({})
    raw_categories = await cursor.to_list(length=None)
    category_list = [serialize_category(cat) for cat in raw_categories]

    return templates.TemplateResponse(
        "partials/home/dashboard/dashboard.html",
        {"request": request, "categories": category_list}
    )
