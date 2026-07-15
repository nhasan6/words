from pydantic import BaseModel
from src.schemas.source import SourceBase, SourceResponse, SourceUpdate

class TvShowBase(SourceBase):
    franchise: str | None = None 
    episode_number: int | None = None
    season_number: int | None = None
    director: str | None = None
    screenwriter: str | None = None 
    actor: str | None = None 
    character: str | None = None # documentaries only have an actor (default to actor over character)

class TvShowCreate(TvShowBase):
    pass

class TvShowResponse(TvShowBase, SourceResponse):
    pass

class TvShowUpdate(SourceUpdate):
    franchise: str | None = None 
    episode_number: int | None = None 
    season_number: int | None = None 
    director: str | None = None 
    screenwriter: str | None = None 
    actor: str | None = None 
    character: str | None = None 