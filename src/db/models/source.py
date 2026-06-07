from typing import List, Optional
from enum import Enum as PyEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Enum as SAEnum, String
from sqlalchemy.dialects.postgresql import ARRAY
from datetime import date
from src.db.models.base import Base

class SourceType(PyEnum):
    book = "book"
    movie = "movie"
    tv_show = "tv_show"
    podcast = "podcast"
    other = "other"

class Source(Base):
    __tablename__ = "sources"
    __mapper_args__ = {
        "polymorphic_on": "type",
        "polymorphic_identity": "source",
    }
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(nullable=False)
    type: Mapped[SourceType] = mapped_column(SAEnum(SourceType)) # want to limit to enums
    quote: Mapped[Optional[str]] = mapped_column()
    genre: Mapped[Optional[List[str]]] = mapped_column(ARRAY(String))
    release_date: Mapped[date] = mapped_column(nullable=False)

    # helper func that makes obj print nicely
    def __repr__(self):
        return f"<Source(id={self.id}, title={self.title}, type={self.type}, genre={self.genre}, release_date={self.release_date})>"
    
