"""
Method 3 — JWT (JSON Web Token)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
After a successful login a signed JWT is issued.  The client stores it
(cookie or localStorage) and sends it on every subsequent request.
The server validates the signature — no DB lookup required per request.

Key concepts:
    • Header   – algorithm (HS256) and token type
    • Payload  – claims: sub (username), exp (expiry timestamp)
    • Signature – HMAC-SHA256(base64(header) + "." + base64(payload), SECRET_KEY)

Required packages (add to requirements.txt):
    python-jose[cryptography]
    passlib[bcrypt]

Your task: implement the 5 TODO functions below.
"""

from fastapi import APIRouter, Depends, Form, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.security import HTTPBearer

from db import SessionDep
from dependencies import templates
from models import UserJWT

router = APIRouter(prefix="/auth/jwt", tags=["Auth – 3. JWT"])

# Configuration — move to environment variables in production
SECRET_KEY = "change-me-before-production"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


@router.get("/login", response_class=HTMLResponse, name="jwt_login_form")
async def jwt_login_form(request: Request):
    # TODO: render templates/auth/jwt_login.html
    pass


@router.post("/login", response_class=HTMLResponse)
async def jwt_login_post(
    request: Request,
    session: SessionDep,
    username: str = Form(...),
    password: str = Form(...),
):
    # TODO:
    # 1. Verify password using passlib:
    #       from passlib.context import CryptContext
    #       pwd_context = CryptContext(schemes=["bcrypt"])
    #       pwd_context.verify(password, user.hashed_password)
    # 2. If invalid → render template with error
    # 3. Build token payload:
    #       from datetime import datetime, timedelta
    #       expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    #       payload = {"sub": username, "exp": expire}
    # 4. Sign token:
    #       from jose import jwt
    #       token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    # 5. Return response and set cookie:
    #       response = RedirectResponse(url="/dashboard", status_code=303)
    #       response.set_cookie(key="access_token", value=token, httponly=True)
    pass


@router.get("/register", response_class=HTMLResponse, name="jwt_register_form")
async def jwt_register_form(request: Request):
    # TODO: render templates/auth/jwt_login.html (or a separate register template)
    pass


@router.post("/register", response_class=HTMLResponse)
async def jwt_register_post(
    request: Request,
    session: SessionDep,
    username: str = Form(...),
    password: str = Form(...),
):
    # TODO:
    # 1. Check uniqueness
    # 2. Hash password:  pwd_context.hash(password)
    # 3. Create UserJWT and commit
    # 4. Redirect to login
    pass


@router.get("/protected", response_class=HTMLResponse, name="jwt_protected")
async def jwt_protected(request: Request, session: SessionDep):
    # TODO:
    # 1. Extract token from cookie:  token = request.cookies.get("access_token")
    # 2. Decode:  from jose import jwt, JWTError
    #             payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    #             username = payload.get("sub")
    # 3. If invalid/expired → redirect to login with error
    # 4. Load user from DB and render a protected page
    pass
