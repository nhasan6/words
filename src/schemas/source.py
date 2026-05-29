from typing import Optional
from datetime import date
from pydantic import BaseModel
from src.db.models.source import SourceType
from src.schemas.word import WordResponse

class SourceBase(BaseModel):
    title: str
    type: SourceType
    quote: Optional[str]
    genre: Optional[list[str]]
    release_date: date

class SourceResponse(SourceBase):
    id: int
    class Config: from_attributes = True


