from fastapi.staticfiles import StaticFiles
from app.routers.pages import home
from fastapi import FastAPI

app = FastAPI()

#estáticos
app.mount("/static", StaticFiles(directory="app/static"), name="static")


# páginas
app.include_router(home.router)

