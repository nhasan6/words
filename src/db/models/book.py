from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from src.db.models.source import Source

class Book(Source):
    __tablename__ = "books"
    __mapper_args__ = {
        "polymorphic_identity": "book",
    }
    # Database level: foreign key column pointing to sources.id
    id: Mapped[int] = mapped_column(ForeignKey("sources.id"), primary_key=True)
    franchise: Mapped[Optional[str]] = mapped_column()
    author: Mapped[str] = mapped_column()
    character: Mapped[Optional[str]] = mapped_column() # not every quote has a named character

    # helper func that makes obj print nicely
    def __repr__(self):
        return (f"<Book(id={self.id}, title={self.title}, " 
                f"type={self.type}, release_date={self.release_date}, "
                f"franchise={self.franchise}, author={self.author}, "
                f"character={self.character}, genre={self.genre})>"
                )
