import bcrypt
from fastapi import APIRouter, Form, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlmodel import select
from db import SessionDep
from dependencies import templates
from models import UserHashed

router = APIRouter(prefix="/auth/hashed", tags=["Auth – 2. Hashed "])


def generate_hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8') 

def verifying_password(password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(password=
        password.encode('utf-8'), hashed_password=
        hashed_password.encode('utf-8')
    )


@router.get("/dashboard", response_class=HTMLResponse, include_in_schema=False)
async def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})


@router.get("/login", include_in_schema=False, name="hashed_login_form")
async def login(request: Request):
    message = request.query_params.get("message")
    return templates.TemplateResponse(
        "auth/hashed_login.html", {"request": request, "message": message}
    )


@router.post(
    "/login",
    response_class=HTMLResponse,
    include_in_schema=False,
    name="hashed_login_post",
)
async def login_post(
    request: Request,
    session: SessionDep,
    username: str = Form(...),
    password: str = Form(...),
):
    user_db = session.exec(
        select(UserHashed).where(UserHashed.username == username)
    ).one_or_none()
    if (
        user_db is None
        or verifying_password(password=password, hashed_password=user_db.hashed_password) == False
    ):
        return templates.TemplateResponse(
            "auth/hashed_login.html",
            {"request": request, "error": "Invalid username or password."},
            status_code=status.HTTP_401_UNAUTHORIZED,
        )

    return RedirectResponse(url="/dashboard", status_code=303)


@router.get("/register", response_class=HTMLResponse, name="hashed_register_form")
async def hashed_register_form(request: Request):
    message = request.query_params.get("message")
    return templates.TemplateResponse(
        "auth/hashed_register.html", {"request": request, "message": message}
    )


@router.post("/register", response_class=HTMLResponse)
async def hashed_register_post(
    request: Request,
    session: SessionDep,
    username: str = Form(...),
    password: str = Form(...),
):
    user_db = session.exec(
        select(UserHashed).where(UserHashed.username == username)
    ).first()
    if user_db:
        return templates.TemplateResponse(
            "auth/hashed_register.html",
            {"request": request, "error": "Username already taken."},
            status_code=status.HTTP_409_CONFLICT,
        )
    hashed_password = generate_hash_password(password=password)
    user = UserHashed(username=username, hashed_password=hashed_password)
    session.add(user)
    session.commit()
    return RedirectResponse(
        url="/auth/hashed/login?message=User+created+successfully",
        status_code=status.HTTP_303_SEE_OTHER,
    )
