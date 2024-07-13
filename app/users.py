from fastapi import Depends
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import JWTStrategy, CookieTransport
from fastapi_users.db import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession
from .models import User as UserModel
from .schemas import UserCreate, UserUpdate, UserRead
from .database import get_async_session
from decouple import config

SECRET_KEY = config("SECRET_KEY")

cookie_transport = CookieTransport(cookie_max_age=3600)
jwt_strategy = JWTStrategy(secret=SECRET_KEY, lifetime_seconds=3600)

auth_backends = [
    cookie_transport.with_strategy(jwt_strategy)
]

async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(UserRead, session, UserModel)

fastapi_users = FastAPIUsers[UserModel, UserCreate, UserUpdate, UserRead](
    get_user_db,
    auth_backends,
)

current_active_user = fastapi_users.current_user(active=True)
