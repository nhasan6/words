from typing import Optional, List
from enum import Enum as PyEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, func, Enum as SAEnum, String
from sqlalchemy.dialects.postgresql import ARRAY
from datetime import datetime
from src.db.models import Base, Source

class WordType(PyEnum):
    noun = "noun"
    verb = "verb"
    adjective = "adjective"
    adverb = "adverb"
    phrase = "phrase"
    idiom = "idiom"
    other = "other"

class Word(Base):
    __tablename__ = "words"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    text: Mapped[str] = mapped_column(unique=True, nullable=False)
    type: Mapped[Optional[WordType]] = mapped_column(SAEnum(WordType)) # want to limit to enums
    etymology: Mapped[Optional[str]] = mapped_column() 
    date_added: Mapped[datetime] = mapped_column(server_default=func.now())
    tags: Mapped[Optional[List[str]]] = mapped_column(ARRAY(String))

    # Database level: foreign key column pointing to sources.id
    source_id: Mapped[Optional[int]] = mapped_column(ForeignKey("sources.id"))

    # SQLAlchemy relationship: links to the Source model ("back_populates" syncs changes on both sides in Python memory)
    source: Mapped[Optional["Source"]] = relationship(back_populates="words")

    # helper func that makes obj print nicely
    def __repr__(self):
        return f"<Word(id={self.id}, text={self.text}, type={self.type}, etymology={self.etymology}, date_added={self.date_added}, tags={self.tags})>"