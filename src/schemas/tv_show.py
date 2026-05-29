from pydantic import BaseModel
from src.schemas.source import SourceBase, SourceResponse
from typing import Optional

class TvShowBase(SourceBase):
    franchise: Optional[str]
    episode_number: int
    season_number: int
    director: str
    screenwriter: Optional[str]
    actor: str
    character: str

class TvShowCreate(TvShowBase):
    pass

class TvShowResponse(TvShowBase, SourceResponse):
    pass
