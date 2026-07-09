from pydantic import BaseModel
from src.schemas.source import SourceBase, SourceResponse, SourceUpdate

class MovieBase(SourceBase):
    franchise: str | None = None 
    director: str | None = None 
    screenwriter: str | None = None 
    actor: str | None = None 
    character: str | None = None 

class MovieCreate(MovieBase):
    pass

class MovieResponse(MovieBase, SourceResponse):
    pass

class MovieUpdate(SourceUpdate):
    franchise: str | None = None 
    director: str | None = None 
    screenwriter: str | None = None 
    actor: str | None = None 
    character: str | None = None 