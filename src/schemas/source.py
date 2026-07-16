from datetime import date
from pydantic import BaseModel
from src.db.models.source import SourceType

class SourceBase(BaseModel):
    title: str
    franchise: str | None = None 
    type: SourceType | None = None
    genre: list[str] | None = None 
    release_date: date | None = None 

class SourceResponse(SourceBase):
    id: int
    model_config = {
        "from_attributes": True
    }

class SourceUpdate(BaseModel):
    title: str | None = None 
    franchise: str | None = None 
    type: SourceType | None = None 
    genre: list[str] | None = None 
    release_date: date | None = None 