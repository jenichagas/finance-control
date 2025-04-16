from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routers.pages import page_home
from app.routers.pages import page_dashboard
from app.routers.auth import auth_login
from app.routers.auth import auth_login as auth_login
from app.routers.pages import page_login as page_login



app = FastAPI()

#estáticos
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# páginas
app.include_router(page_home.router)
app.include_router(page_dashboard.router)
app.include_router(auth_login.router)
app.include_router(page_login.router)
