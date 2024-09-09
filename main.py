from fastapi import FastAPI

from fastapi_async_sqlalchemy import SQLAlchemyMiddleware, db

from contextlib import asynccontextmanager
from dotenv import load_dotenv
import os

from src.configs.database import Base

load_dotenv()

DB_URL = os.getenv("DB_URL")


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db():
        await db.session.run_sync(Base.metadata.create_all)
        yield


async def get_db():
    async with db():
        yield db.session



app = FastAPI(lifespan=lifespan)


app.add_middleware(
    SQLAlchemyMiddleware,
    db_url=os.environ.get("DB_URL"),
    engine_args={
        "echo": True,
        "pool_pre_ping": True,
        "pool_size": 5,
        "max_overflow": 10,
    },

)
