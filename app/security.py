from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from decouple import config
from typing import AsyncGenerator

DATABASE_URL = config("DATABASE_URL")

engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)
Base = declarative_base()

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        yield session
