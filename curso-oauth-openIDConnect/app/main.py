from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from db import create_all_tables
from dependencies import templates
from auth_methods.basic import router as basic_router
from auth_methods.hashed import router as hashed_router
from auth_methods.jwt_auth import router as jwt_router
from auth_methods.oauth2 import router as oauth2_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    next(create_all_tables(app))
    yield


app = FastAPI(
    title="Auth Methods — Learning Project",
    description=(
        "Explore authentication methods from least secure to industry standard. "
        "Open / in a browser to see the interactive panel."
    ),
    version="2.0.0",
    lifespan=lifespan,
)

BASE_DIR = Path(__file__).resolve().parent
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")

app.include_router(basic_router)
app.include_router(hashed_router)
app.include_router(jwt_router)
app.include_router(oauth2_router)



@app.get("/", response_class=HTMLResponse, include_in_schema=False, name="home")
async def home(request: Request):
    return templates.TemplateResponse("auth/index.html", {"request": request})


@app.get("/dashboard", response_class=HTMLResponse, include_in_schema=False)
async def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})
