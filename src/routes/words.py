from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from src.auth.dependencies import get_current_user
from src.db.connection import get_db
from sqlalchemy import select

from src.db.models.book import Book
from src.db.models.movie import Movie
from src.db.models.source import Source, SourceType
from src.db.models.tv_show import TvShow
from src.filters.filters import apply_filters
from src.schemas.filter import WordFilter
from src.schemas.word import WordCreate, WordResponse, WordUpdate
from src.db.models.word import Word

router = APIRouter(prefix="/words")

@router.get("/", response_model=list[WordResponse])
async def get_words(filters: WordFilter = Depends(), db: AsyncSession = Depends(get_db)) -> list[WordResponse]:
    stmt = select(Word).join(Source)
    stmt = apply_filters(stmt, filters)
    result = await db.execute(stmt)
    return result.scalars().all()

@router.get("/{id}", response_model=WordResponse)
async def get_word(id: int, db: AsyncSession = Depends(get_db)) -> WordResponse:
    result = await db.get(Word, id)

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Word not found"
        )
    return result

@router.post("/", response_model=WordResponse)
async def add_word(word: WordCreate, db: AsyncSession = Depends(get_db), current_user = Depends(get_current_user)) -> WordResponse:
    if word.source_id:
        source = await db.get(Source, word.source_id)
        if source is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Source not found"  # source doesn't exist (needs to be created first)
            )
    new_word = Word(
        text = word.text,
        type = word.type,
        etymology = word.etymology,
        tags = word.tags,
        source_id = word.source_id
    )
    try:
        db.add(new_word)
        await db.commit()
        await db.refresh(new_word)
        return new_word
    except Exception:
        await db.rollback() # undoes any partial changes
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occured"
        )
    
@router.put("/{id}", response_model=WordResponse)
async def update_word(id: int, word: WordUpdate, db: AsyncSession = Depends(get_db), current_user = Depends(get_current_user)) -> WordResponse:
    db_word = await db.get(Word, id)
    if db_word is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Word not found"
        )
    
    if word.source_id:
        source = await db.get(Source, word.source_id)
        if source is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Source not found"  # source doesn't exist (needs to be created first)
            )

    update_data = word.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_word, key, value)

    await db.commit()
    await db.referesh(db_word)

    return db_word
