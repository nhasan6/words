from src.schemas.source import SourceBase, SourceResponse
from typing import Optional

class BookBase(SourceBase):
    franchise: Optional[str]
    author: str
    character: Optional[str]

class BookCreate(BookBase):
    pass

class BookResponse(BookBase, SourceResponse):
    pass
