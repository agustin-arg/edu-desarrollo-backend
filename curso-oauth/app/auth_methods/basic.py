"""
Method 1 — Basic (Plain Text)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️  MOST INSECURE: passwords are stored and compared as plain text.
    This method exists purely for educational comparison.
    Never use plain-text passwords in production.

How it works:
    1. User registers → password saved to DB as-is (no transformation).
    2. User logs in   → submitted password is compared directly to stored value.

Your task: implement the 4 TODO functions below.
"""

from fastapi import APIRouter, Form, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlmodel import select

from db import SessionDep
from dependencies import templates
from models import UserPlain

router = APIRouter(prefix="/auth/basic", tags=["Auth – 1. Basic (Plain Text)"])


@router.get("/dashboard", response_class=HTMLResponse, include_in_schema=False)
async def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})


@router.get("/login", include_in_schema=False, name="basic_login_form")
async def login(request: Request):
    message = request.query_params.get("message")
    return templates.TemplateResponse(
        "auth/basic_login.html", {"request": request, "message": message}
    )


@router.post(
    "/login",
    response_class=HTMLResponse,
    include_in_schema=False,
    name="basic_login_post",
)
async def login_post(
    request: Request,
    session: SessionDep,
    username: str = Form(...),
    password: str = Form(...),
):
    user_db = session.exec(
        select(UserPlain).where(UserPlain.username == username)
    ).one_or_none()

    # Plain text comparison — no hashing (that's the whole point of this method)
    if user_db is None or user_db.password != password:
        return templates.TemplateResponse(
            "auth/basic_login.html",
            {"request": request, "error": "Invalid username or password."},
            status_code=status.HTTP_401_UNAUTHORIZED,
        )

    return RedirectResponse(url="/dashboard", status_code=303)


@router.get("/register", response_class=HTMLResponse, name="basic_register_form")
async def basic_register_form(request: Request):
    message = request.query_params.get("message")
    return templates.TemplateResponse(
        "auth/basic_register.html", {"request": request, "message": message}
    )


@router.post("/register", response_class=HTMLResponse)
async def basic_register_post(
    request: Request,
    session: SessionDep,
    username: str = Form(...),
    password: str = Form(...),
):
    user_db = session.exec(
        select(UserPlain).where(UserPlain.username == username)
    ).first()
    if user_db:
        return templates.TemplateResponse(
            "auth/basic_register.html",
            {"request": request, "error": "Username already taken."},
            status_code=status.HTTP_409_CONFLICT,
        )
    user = UserPlain(username=username, password=password)
    session.add(user)
    session.commit()
    # PRG: redirect to GET /login so a browser refresh doesn't resubmit the form
    return RedirectResponse(
        url="/auth/basic/login?message=User+created+successfully",
        status_code=status.HTTP_303_SEE_OTHER,
    )
