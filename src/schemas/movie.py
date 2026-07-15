from pydantic import BaseModel
from src.schemas.source import SourceBase, SourceResponse, SourceUpdate

class MovieBase(SourceBase):
    director: str | None = None 
    screenwriter: str | None = None 
    cast: list[str] | None = None

class MovieCreate(MovieBase):
    pass

class MovieResponse(MovieBase, SourceResponse):
    pass

class MovieUpdate(SourceUpdate):
    director: str | None = None 
    screenwriter: str | None = None 
    cast: list[str] | None = None
