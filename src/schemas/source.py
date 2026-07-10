from datetime import date
from pydantic import BaseModel
from src.db.models.source import SourceType

class SourceBase(BaseModel):
    title: str
    type: SourceType
    quote: str | None = None 
    genre: list[str] | None = None 
    release_date: date | None = None 

class SourceResponse(SourceBase):
    id: int
    model_config = {
        "from_attributes": True
    }

class SourceUpdate(BaseModel):
    title: str | None = None 
    type: SourceType | None = None 
    quote: str | None = None 
    genre: list[str] | None = None 
    release_date: date | None = None 