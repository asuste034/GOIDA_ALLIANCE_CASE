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

@app.post("/users/", response_model=UserResponse)
async def create_user(
    user: UserCreate,
    session: AsyncSession = Depends(get_session)
    ):
    """Создание нового пользователя"""
    try:
        async with session.begin():
            new_user = User(**user.model_dump())
            session.add(new_user)
        await session.refresh(new_user)
        return new_user
    except IntegrityError:
        raise HTTPException(
            status_code=400,
            detail="Пользователь с таким email уже есть в базе"
        )

@app.post("/login", response_model=Token)
async def login(data: UserCreate, db: AsyncSession = Depends(get_session())):
    result = await db.execute(select(User).where(User.username == data.username))
    user = result.scalar_one_or_none()
    if not user or not verify_password(data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    token = create_access_token({"sub": str(user.id)})
    return Token(access_token=token)


@app.get("/users/", response_model=list[UserResponse])
async def list_users(session: AsyncSession = Depends(get_session)):
    """Все пользователи что есть в бд"""
    result = await session.execute(select(User))
    users = result.scalars().all()
    return users