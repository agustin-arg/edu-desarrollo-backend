"""
Database models — one table per authentication method.

Each model isolates the user data for that method so you can study
each approach independently without sharing state between them.
"""

from typing import Optional

from sqlmodel import Field, SQLModel


# Method 1 – Plain Text (most insecure)


class UserPlain(SQLModel, table=True):
    """⚠️  Stores passwords as plain text. NEVER do this in production."""

    __tablename__ = "user_plain"

    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(unique=True, min_length=3, max_length=50)
    password: str  # plain text — stored exactly as the user typed it


# Method 2 –  Hashed


class UserHashed(SQLModel, table=True):
    """Stores passwords as a  hex digest (better, but not production-ready)."""

    __tablename__ = "user_hashed"

    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(unique=True, min_length=3, max_length=50)
    hashed_password: str  #  hex string


# Method 3 – JWT


class UserJWT(SQLModel, table=True):
    """Credentials for JWT-based authentication (bcrypt hashing recommended)."""

    __tablename__ = "user_jwt"

    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(unique=True, min_length=3, max_length=50)
    hashed_password: str  # use passlib bcrypt: pwd_context.hash(password)


# Method 4 – OAuth2 Password Flow


class UserOAuth2(SQLModel, table=True):
    """Credentials for the OAuth2 password flow (Bearer token)."""

    __tablename__ = "user_oauth2"

    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(unique=True, min_length=3, max_length=50)
    hashed_password: str  # use passlib bcrypt
    is_active: bool = Field(default=True)


# API Schemas for router/users.py (JSON CRUD)


class UserHashedCreate(SQLModel):
    username: str = Field(min_length=3, max_length=50)
    password: str = Field(min_length=8)


class UserHashedUpdate(SQLModel):
    username: Optional[str] = Field(default=None, min_length=3, max_length=50)
    password: Optional[str] = Field(default=None, min_length=8)
    is_active: Optional[bool] = None


class UserHashedResponse(SQLModel):
    id: int
    username: str
