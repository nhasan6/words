from pydantic import BaseModel
from src.schemas.source import SourceBase, SourceResponse, SourceUpdate

class TvShowBase(SourceBase):
    episode_number: int | None = None
    season_number: int | None = None
    director: str | None = None
    screenwriter: str | None = None 
    cast: list[str] | None = None

class TvShowCreate(TvShowBase):
    pass

class TvShowResponse(TvShowBase, SourceResponse):
    pass

class TvShowUpdate(SourceUpdate):
    episode_number: int | None = None 
    season_number: int | None = None 
    director: str | None = None 
    screenwriter: str | None = None 
    cast: list[str] | None = None