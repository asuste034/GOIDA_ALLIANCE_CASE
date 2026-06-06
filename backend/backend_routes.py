# routes todo: create, edit, delete, save, select
# preview, CHS
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from backend import database
from backend.database import get_session
from backend.main import app
from backend.models import Block, Events


@app.post('/event', response_model=list[Events])
async def create_event(event: Events, db: AsyncSession = Depends(get_session())):
    return await database.create_event(db, event)


@app.get('/events', response_model=list[Events])
async def get_events(db: AsyncSession = Depends(get_session())):
    return database.get_events(db)


