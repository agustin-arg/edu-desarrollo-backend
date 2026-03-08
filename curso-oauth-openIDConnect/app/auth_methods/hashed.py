"""
Method 2 — Hashed (SHA-256)
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Passwords are never stored in plain text; they are transformed into a
SHA-256 hex digest before being saved.  At login time the submitted
password is hashed with the same algorithm and compared to the stored hash.

Better than plain text, but SHA-256 is a fast hash → still vulnerable to
brute-force and rainbow-table attacks at scale.  For real apps use bcrypt.

How it works:
    Register: hash(password) → store digest
    Login:    hash(submitted_password) == stored_hash ?

Your task: implement the 4 TODO functions below.
Helper already provided: _hash_password(plain: str) → str
"""

import hashlib

from fastapi import APIRouter, Form, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlmodel import select

from db import SessionDep
from dependencies import templates
from models import UserHashed

router = APIRouter(prefix="/auth/hashed", tags=["Auth – 2. Hashed (SHA-256)"])


def _hash_password(plain: str) -> str:
    """Return the SHA-256 hex digest of a plain-text password."""
    return hashlib.sha256(plain.encode()).hexdigest()


@router.get("/login", response_class=HTMLResponse, name="hashed_login_form")
async def hashed_login_form(request: Request):
    # TODO: render templates/auth/hashed_login.html
    # Hint: pass "message" from query params for flash messages
    #   message = request.query_params.get("message")
    pass


@router.post("/login", response_class=HTMLResponse)
async def hashed_login_post(
    request: Request,
    session: SessionDep,
    username: str = Form(...),
    password: str = Form(...),
):
    # TODO:
    # 1. Query DB for UserHashed by username
    # 2. Hash the submitted password:  hashed = _hash_password(password)
    # 3. If user is None or user.hashed_password != hashed → render template with error
    # 4. If match → RedirectResponse(url="/dashboard", status_code=303)
    pass


@router.get("/register", response_class=HTMLResponse, name="hashed_register_form")
async def hashed_register_form(request: Request):
    # TODO: render templates/auth/hashed_register.html
    pass


@router.post("/register", response_class=HTMLResponse)
async def hashed_register_post(
    request: Request,
    session: SessionDep,
    username: str = Form(...),
    password: str = Form(...),
):
    # TODO:
    # 1. Check uniqueness → re-render with error if taken
    # 2. Create:  UserHashed(username=username, hashed_password=_hash_password(password))
    # 3. session.add(user); session.commit()
    # 4. RedirectResponse to /auth/hashed/login?message=Account+created
    pass
