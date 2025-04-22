from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# Páginas
from app.routers.pages import page_home, page_dashboard, page_login, page_register, page_reset, page_profile_user

# Autenticação (API)
from app.routers.auth import auth_login, auth_register, auth_reset


app = FastAPI()

# arquivos estáticos
app.mount("/statics", StaticFiles(directory="app/templates/statics"), name="statics")

# páginas (HTML)
app.include_router(page_home.router)
app.include_router(page_dashboard.router)
app.include_router(page_login.router)
app.include_router(page_register.router)
app.include_router(page_reset.router)
app.include_router(page_profile_user.router)



# rotas de API (ex: login, reset)
app.include_router(auth_login.router)
app.include_router(auth_reset.router)
app.include_router(auth_register.router)


