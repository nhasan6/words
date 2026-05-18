from typing import Optional

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import func, Enum
from datetime import datetime
from src.db.models.base import Base
from enum import Enum

class WordType(Enum):
    noun = "noun"
    verb = "verb"
    adjective = "adjective"
    adverb = "adverb"
    phrase = "phrase"
    idiom = "idiom"
    other = "other"

class Word(Base):
    __tablename__ = "words"
    id: Mapped[int] = mapped_column(primary_key = True, autoincrement=True)
    text: Mapped[str] = mapped_column(unique=True, nullable=False)
    type: Mapped[Optional[WordType]] = mapped_column(Enum(WordType)) # want to limit to enums
    etymology: Mapped[str] = mapped_column() # want to limit to enums
    date_added: Mapped[datetime] = mapped_column(server_default=func.now())
    tags: Mapped[list]




    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    # helper func that makes obj print nicely
    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email})>"