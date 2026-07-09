from pydantic import BaseModel
from datetime import datetime
from src.db.models.word import WordType
from src.schemas.source import SourceResponse

class WordBase(BaseModel):
    text: str
    type: WordType | None = None
    etymology: str | None = None
    tags: list[str] | None = None

class WordCreate(WordBase):
    source_id: int | None = None

class WordUpdate(BaseModel):
    text: str | None = None
    type: WordType | None = None
    etymology: str | None = None
    tags: list[str] | None = None
    source_id: int | None = None

class WordResponse(WordBase):
    id: int
    date_added: datetime
    source: SourceResponse | None = None
    model_config = {
        "from_attributes": True
    }

