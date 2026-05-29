from typing import Optional

from pydantic import BaseModel
from datetime import datetime
from src.db.models.word import WordType
from src.schemas.source import SourceResponse

class WordBase(BaseModel):
    text: str
    type: Optional[WordType]
    etymology: Optional[str]
    tags: Optional[list[str]]

class WordCreate(WordBase):
    source_id: Optional[int]

class WordResponse(WordBase):
    id: int
    date_added: datetime
    source: Optional[SourceResponse]
    class Config: from_attributes = True


