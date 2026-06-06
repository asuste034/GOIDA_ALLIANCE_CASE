# routes todo: create, edit, delete, save, select
# preview, CHS

from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db import database
from db.database import get_session
from db.models import  Events, EventResponse

router = APIRouter(prefix="/events", tags=["events"])

@router.post('/events', response_model=EventResponse)
async def create_event(event: Events, db: AsyncSession = Depends(get_session())):
    return await database.create_event(db, event)


@router.get('/events', response_model=list[EventResponse])
async def get_events(db: AsyncSession = Depends(get_session())):
    return database.get_events(db)

@router.put('/events/{event_id}', response_model=EventResponse)
async def update_event(event_id: int, updates: Events, db : AsyncSession = Depends(get_session)):
    event = await database.update_event(db, event_id, updates)
    if not event:
        raise HTTPException(status_code=404, detail="ШАБЛОН НЕ НАЙДЕН")
    return event

@router.delete('/events/{event_id}', response_model=EventResponse)
async def delete_event(event_id: int, db : AsyncSession = Depends(get_session())):
    event = await database.delete_event(db, event_id)
    if not event:
        raise HTTPException(status_code=404, detail="ШАБЛОН НЕ НАЙДЕН")
    return {"message" : "Шаблон удален успешно"}

@router.get('/events/{event_id}', response_model=EventResponse)
async def get_event(event_id: int, db: AsyncSession = Depends(get_session())):
    return await database.get_event_by_id(db, event_id)