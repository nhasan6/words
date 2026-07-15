from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from src.auth.dependencies import get_current_user
from src.db.connection import get_db
from sqlalchemy import select

from src.db.models.book import Book
from src.db.models.movie import Movie
from src.db.models.source import Source, SourceType
from src.db.models.tv_show import TvShow
from src.schemas.book import BookCreate, BookResponse, BookUpdate
from src.schemas.movie import MovieCreate, MovieResponse, MovieUpdate
from src.schemas.source import SourceResponse, SourceBase
from src.schemas.tv_show import TvShowCreate, TvShowResponse, TvShowUpdate

router = APIRouter(prefix="/sources")

@router.get("/", response_model=list[SourceResponse])
async def get_sources(db: AsyncSession = Depends(get_db)) -> list[SourceResponse]:
    result = await db.execute(select(Source).execution_options(populate_existing=True))
    return result.scalars().all()

@router.get("/{id}", response_model=SourceResponse,
            responses={ 404: {"description": "Source not found"} } )
async def get_source(id: int, db: AsyncSession = Depends(get_db)) -> SourceResponse:
    result = await db.get(Source, id)

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Source not found"
        )
    return result

@router.post("/book", response_model=BookResponse, status_code=status.HTTP_201_CREATED,
             responses={ 
                 401: {"description": "Not authenticated"},
                 500: {"description": "Database error"}} )
async def add_book(book: BookCreate, db: AsyncSession = Depends(get_db), _current_user = Depends(get_current_user)) -> BookResponse:
    new_book = Book(
        title = book.title,
        type = SourceType.book,
        quote = book.quote,
        genre = book.genre,
        release_date = book.release_date,

        franchise = book.franchise,
        author = book.author,
        character = book.character
    )
    try:
        db.add(new_book)
        await db.commit()
        await db.refresh(new_book)
        return new_book
    except SQLAlchemyError:
        await db.rollback() # undoes any partial changes
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database error"
        )
    
@router.post("/movie", response_model=MovieResponse, status_code=status.HTTP_201_CREATED,
             responses={ 
                 401: {"description": "Not authenticated"},
                 500: {"description": "Database error"}} )
async def add_movie(movie: MovieCreate, db: AsyncSession = Depends(get_db), _current_user = Depends(get_current_user)) -> MovieResponse:
    new_movie = Movie(
        title = movie.title,
        type = SourceType.movie,
        quote = movie.quote,
        genre = movie.genre,
        release_date = movie.release_date,

        franchise = movie.franchise,
        director = movie.director,
        screenwriter = movie.screenwriter,
        actor = movie.actor,
        character = movie.character
    )

    try:
        db.add(new_movie)
        await db.commit()
        await db.refresh(new_movie)
        return new_movie
    except SQLAlchemyError:
        await db.rollback() # undoes any partial changes
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database error"
        )
    
@router.post("/tv", response_model=TvShowResponse, status_code=status.HTTP_201_CREATED,
             responses={ 
                 401: {"description": "Not authenticated"},
                 500: {"description": "Database error"}} )
async def add_tv_show(tv_show: TvShowCreate, db: AsyncSession = Depends(get_db), _current_user = Depends(get_current_user)) -> TvShowResponse:
    new_tv_show = TvShow(
        title = tv_show.title,
        type = SourceType.tv_show,
        quote = tv_show.quote,
        genre = tv_show.genre,
        release_date = tv_show.release_date,

        franchise = tv_show.franchise,
        director = tv_show.director,
        episode_number = tv_show.episode_number,
        season_number = tv_show.season_number,
        screenwriter = tv_show.screenwriter,
        actor = tv_show.actor,
        character = tv_show.character
    )

    try:
        db.add(new_tv_show)
        await db.commit()
        await db.refresh(new_tv_show)
        return new_tv_show
    except SQLAlchemyError:
        await db.rollback() # undoes any partial changes
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database error"
        )

@router.put("/tv/{id}", response_model=TvShowResponse, 
            responses={
                401: {"description": "Not authenticated"},
                404: {"description": "Source not found"},
                500: {"description": "Database error"} })
async def update_tv_show(id: int, tv_show: TvShowUpdate, db: AsyncSession = Depends(get_db), _current_user = Depends(get_current_user)) -> TvShowResponse:
    db_tv_show = await db.get(Source, id)
    if db_tv_show is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Source not found"
        )
    
    update_data = tv_show.model_dump(exclude_unset=True)

    try: 

        for key, value in update_data.items():
            setattr(db_tv_show, key, value)

        await db.commit()
        await db.refresh(db_tv_show)
        return db_tv_show
    
    except SQLAlchemyError:
        await db.rollback() # undoes any partial changes
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database Error"
        )
    
@router.put("/movie/{id}", response_model=MovieResponse, 
            responses={
                401: {"description": "Not authenticated"},
                404: {"description": "Source not found"},
                500: {"description": "Database error"} })
async def update_movie(id: int, movie: MovieUpdate, db: AsyncSession = Depends(get_db), _current_user = Depends(get_current_user)) -> MovieResponse:
    db_movie = await db.get(Source, id)
    if db_movie is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Source not found"
        )
    
    update_data = movie.model_dump(exclude_unset=True)

    try: 

        for key, value in update_data.items():
            setattr(db_movie, key, value)

        await db.commit()
        await db.refresh(db_movie)
        return db_movie
    
    except SQLAlchemyError:
        await db.rollback() # undoes any partial changes
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database Error"
        )

@router.put("/book/{id}", response_model=BookResponse, 
            responses={
                401: {"description": "Not authenticated"},
                404: {"description": "Source not found"},
                500: {"description": "Database error"} })
async def update_book(id: int, book: BookUpdate, db: AsyncSession = Depends(get_db), _current_user = Depends(get_current_user)) -> BookResponse:
    db_book = await db.get(Source, id)
    if db_book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Source not found"
        )
    
    update_data = book.model_dump(exclude_unset=True)

    try: 

        for key, value in update_data.items():
            setattr(db_book, key, value)

        await db.commit()
        await db.refresh(db_book)
        return db_book
    
    except SQLAlchemyError:
        await db.rollback() # undoes any partial changes
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database Error"
        )