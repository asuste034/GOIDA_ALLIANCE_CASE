from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db.database import AsyncSessionLocal
from db.models import Events


async def get_session() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session

async def create_event(db: AsyncSession, event: Events):
    db.add(event)
    await db.flush()
    await db.commit()
    await db.refresh(event)
    return event

async def delete_event(db: AsyncSession, event: Events):
    await db.delete(event)
    await db.flush()
    await db.commit()

async def update_event(db: AsyncSession, id : int, updates: Events):
    event = await get_event_by_id(db, id)
    if not event:
        return None
    update_data = updates.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(event, key, value)
    await db.commit()
    await db.refresh(event)
    return event

async def get_event_by_id(db: AsyncSession, id : int):
    result = await db.execute(
        select(Events).where(
            Events.id == id
        )
    )
    return result.scalar_one_or_none()

async def get_events(db: AsyncSession):
    result = await db.execute(
        select(Events)
    )
    return result.scalars().all()