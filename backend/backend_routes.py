# routes todo: create, edit, delete, save, select
# preview, CHS
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from backend.database import get_session
from backend.main import app
from backend.models import Block, Events


# @app.post('/event', response_model=list[Events])
# async def create_blocks(event: Events, db: AsyncSession = Depends(get_session())):
#
#
