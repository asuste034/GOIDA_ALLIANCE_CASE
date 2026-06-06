from tokenize import Token

from fastapi import Depends, FastAPI
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from starlette import status

from backend.utils import verify_password, create_access_token
from deps import get_session
from models import User, UserCreate, UserResponse

from contextlib import asynccontextmanager
@asynccontextmanager
async def lifespan(app: FastAPI):
    from init_db import init_models
    await init_models()
    yield

app = FastAPI(lifespan=lifespan)
