from sqlalchemy import Select, func

from src.db.models.book import Book
from src.db.models.movie import Movie
from src.db.models.source import Source, SourceType
from src.db.models.tv_show import TvShow
from src.db.models.word import Word
from src.schemas.filter import WordFilter


def apply_word_filters(stmt: Select, filters: WordFilter):
    if filters.word_type:
        stmt = stmt.where(Word.type == filters.word_type)
    if filters.speaker:
        stmt = stmt.where(Word.speaker.ilike(f"%{filters.speaker}%"))
    return stmt

def apply_source_filters(stmt, filters: WordFilter):
    if filters.title:
        stmt = stmt.where(Source.title.ilike(f"%{filters.title}%"))
    if filters.franchise:
        stmt = stmt.where(Source.franchise.ilike(f"%{filters.franchise}%"))
    if filters.released_after:
        stmt = stmt.where(Source.release_date >= filters.released_after)
    if filters.released_before:
        stmt = stmt.where(Source.release_date <= filters.released_before)
    if filters.genre:
        stmt = stmt.where(
            func.lower(func.array_to_string(Source.genre, ", ")).like(
                f"%{filters.genre.lower()}%"
            )
        )
    return stmt

def apply_book_filters(stmt, filters: WordFilter):
    if filters.author: # don't join if just title
        stmt = stmt.join(Book)
        stmt = stmt.where(Book.author.ilike(f"%{filters.author}%"))
    return stmt

def apply_tv_filters(stmt, filters: WordFilter):
    if filters.director or filters.cast_member: 
        stmt = stmt.join(TvShow)
        if filters.director:
            stmt = stmt.where(TvShow.director.ilike(f"%{filters.director}%"))
        if filters.cast_member:
            stmt = stmt.where(
                func.lower(func.array_to_string(TvShow.cast, ", ")).like(
                    f"%{filters.cast_member.lower()}%"
                )
            )
    return stmt

def apply_movie_filters(stmt, filters: WordFilter):
    if filters.director or filters.cast_member: 
        stmt = stmt.join(Movie)

        if filters.director:
            stmt = stmt.where(Movie.director.ilike(f"%{filters.director}%"))
        if filters.cast_member:
            stmt = stmt.where(
                func.lower(func.array_to_string(TvShow.cast, ", ")).like(
                    f"%{filters.cast_member.lower()}%"
                )
            )
    return stmt
        
def apply_filters(stmt, filters):
    stmt = apply_word_filters(stmt, filters)
    stmt = apply_source_filters(stmt, filters)

    match filters.source_type:
        case SourceType.book:
            stmt = apply_book_filters(stmt, filters)
        case SourceType.movie:
            stmt = apply_movie_filters(stmt, filters)
        case SourceType.tv_show:
            stmt = apply_tv_filters(stmt, filters)
    
    return stmt