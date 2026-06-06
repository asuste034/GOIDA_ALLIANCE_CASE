from sqlite3 import IntegrityError

from fastapi import Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from backend.deps import get_session
from backend.main import app
from backend.models import UserResponse, UserCreate, User, Token
from backend.utils import verify_password, create_access_token


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
    """логин"""
    result = await db.execute(select(User).where(User.username == data.username))
    user = result.scalar_one_or_none()
    if not user or not verify_password(data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Неверные данные")
    token = create_access_token({"sub": str(user.id)})
    return Token(access_token=token)


@app.get("/users/", response_model=list[UserResponse])
async def list_users(session: AsyncSession = Depends(get_session)):
    """Все пользователи что есть в бд"""
    result = await session.execute(select(User))
    users = result.scalars().all()
    return users