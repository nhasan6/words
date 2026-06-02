from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from jwt import InvalidTokenError
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.auth.jwt import ALGORITHM
from src.config import Settings
import jwt
from src.db.connection import get_db

from src.schemas.auth import TokenData
from src.db.models import User

settings = Settings()

# tells fastapi to look for a bearer token in the auth header of incoming requests 
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: AsyncSession = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, # make unauthorized 401 show as 404 not found (security measure)
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # decodes the token using the secret key
        payload = jwt.decode(token, settings.SECRET_JWT_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub") # sub is short for subject (username stored)
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username) # wraps username in TokenData schema
    except InvalidTokenError:
        raise credentials_exception
    result = await db.execute(select(User).where(User.username == token_data.username))
    user = result.scalar_one_or_none()
    if user is None:
        raise credentials_exception
    return user


# async def get_current_active_user(
#     current_user: Annotated[User, Depends(get_current_user)],
# ):
#     if current_user.disabled:
#         raise HTTPException(status_code=400, detail="Inactive user")
#     return current_user

