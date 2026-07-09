from pydantic import BaseModel
from datetime import date
from src.db.models.source import SourceType
from src.db.models.word import WordType
from src.schemas.source import SourceBase, SourceResponse, SourceUpdate

class WordFilter(BaseModel):

    word_type: WordType | None = None
    source_type: SourceType | None = None

    title: str | None = None
    genre: str | None = None
    released_after: date | None = None
    released_before: date | None = None

    # book, movie & tv
    character: str | None = None

    # book
    author: str | None = None 

    # movie & tv
    director: str | None = None
    actor: str | None = None

    
