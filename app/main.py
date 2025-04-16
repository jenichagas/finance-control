from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# Páginas
from app.routers.pages import page_home
from app.routers.pages import page_dashboard
from app.routers.pages import page_login
from app.routers.pages import page_register
from app.routers.pages import page_reset


# Autenticação (API)
from app.routers.auth import auth_login, auth_register, auth_reset


app = FastAPI()

# arquivos estáticos
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# páginas (HTML)
app.include_router(page_home.router)
app.include_router(page_dashboard.router)
app.include_router(page_login.router)
app.include_router(page_register.router)
app.include_router(page_reset.router)


# rotas de API (ex: login, reset)
app.include_router(auth_login.router)
app.include_router(auth_reset.router)
app.include_router(auth_register.router)

