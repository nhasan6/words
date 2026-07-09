from src.schemas.source import SourceBase, SourceResponse, SourceUpdate

class BookBase(SourceBase):
    franchise: str | None = None 
    author: str
    character: str | None = None 

class BookCreate(BookBase):
    pass

class BookResponse(BookBase, SourceResponse):
    pass

class BookUpdate(SourceUpdate):
    franchise: str | None = None 
    author: str | None = None 
    character: str | None = None 
