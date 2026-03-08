"""
Method 4 — OAuth2 Password Flow
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Uses FastAPI's built-in OAuth2PasswordBearer + OAuth2PasswordRequestForm.
The POST /token endpoint is the OAuth2 "token endpoint": it receives
username/password and returns a Bearer JWT.

Clients (e.g. the Swagger UI "Authorize" button) send:
    Authorization: Bearer <token>
on subsequent requests, which FastAPI validates via the dependency.

Required packages (add to requirements.txt):
    python-jose[cryptography]
    passlib[bcrypt]

Your task: implement the 4 TODO functions below.
"""

from fastapi import APIRouter, Depends, Form, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from db import SessionDep
from dependencies import templates
from models import UserOAuth2

router = APIRouter(prefix="/auth/oauth2", tags=["Auth – 4. OAuth2 Password Flow"])

# FastAPI will point Swagger UI's "Authorize" to this URL
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/oauth2/token")

SECRET_KEY = "change-me-before-production"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


@router.get("/login", response_class=HTMLResponse, name="oauth2_login_form")
async def oauth2_login_form(request: Request):
    # TODO: render templates/auth/oauth2_login.html
    pass


@router.post("/token", summary="OAuth2 token endpoint")
async def oauth2_token(
    session: SessionDep,
    form_data: OAuth2PasswordRequestForm = Depends(),
):
    # TODO:
    # 1. Look up UserOAuth2 by form_data.username
    # 2. Verify password with passlib: pwd_context.verify(form_data.password, user.hashed_password)
    # 3. If invalid → raise HTTPException(status_code=401, detail="Incorrect credentials",
    #                                      headers={"WWW-Authenticate": "Bearer"})
    # 4. Build and sign JWT (same as Method 3)
    # 5. Return {"access_token": token, "token_type": "bearer"}
    #    ← This exact shape is required by the OAuth2 spec
    pass


@router.get("/register", response_class=HTMLResponse, name="oauth2_register_form")
async def oauth2_register_form(request: Request):
    # TODO: render the register template
    pass


@router.post("/register", response_class=HTMLResponse)
async def oauth2_register_post(
    request: Request,
    session: SessionDep,
    username: str = Form(...),
    password: str = Form(...),
):
    # TODO:
    # 1. Check uniqueness
    # 2. Hash password with bcrypt
    # 3. Create UserOAuth2(username=username, hashed_password=...) and commit
    # 4. Redirect to login
    pass


@router.get("/me", summary="Get current authenticated user")
async def oauth2_me(
    session: SessionDep,
    token: str = Depends(oauth2_scheme),
):
    # TODO:
    # 1. Decode JWT: payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    # 2. Extract username: payload.get("sub")
    # 3. Load UserOAuth2 from DB and return it (use a Pydantic response model)
    pass
