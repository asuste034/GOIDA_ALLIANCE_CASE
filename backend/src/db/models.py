from typing import Optional

from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.event import Events

from backend.src.db.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

class UserCreate(BaseModel):
    name: str
    email: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    class Config:
        from_attributes = True

class Block(BaseModel):
    title: str
    content: str
    date: Optional[str] = None
    image: Optional[str] = None

class EmergencyBlock(BaseModel):
    text: str

class Styles(BaseModel):
    text: str

class Events(BaseModel):
    type: str
    block : Optional[Block]
    emergency_block: Optional[EmergencyBlock]

class EventResponse(Events):
    pass