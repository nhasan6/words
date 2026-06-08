from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.connection import get_db
from sqlalchemy import select

from src.schemas.word import WordResponse
from src.db.models.word import Word

router = APIRouter(prefix="/words")

@router.get("/", response_model=list[WordResponse])
async def get_all_words(db: AsyncSession = Depends(get_db)) -> list[WordResponse]:
    result = await db.execute(select(Word))
    return result.scalars().all()

@router.get("/{id}", response_model=WordResponse)
async def get_word(db: AsyncSession = Depends(get_db)) -> WordResponse:
    result = await db.execute(select(Word))
    return result.scalars().one_or_none()
# should there be an error if not found?

@router.post("/", response_model=WordResponse)
async def add_word(db: AsyncSession = Depends(get_db)) -> WordResponse:
    result = await db.execute(select(Word))
    return result.scalars().one_or_none()





