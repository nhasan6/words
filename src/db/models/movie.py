from typing import List, Optional
from sqlalchemy import ARRAY, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column
from src.db.models.source import Source, SourceType

class Movie(Source):
    __tablename__ = "movies"
    __mapper_args__ = {
        "polymorphic_identity": SourceType.movie
    }
     # Database level: foreign key column pointing to sources.id
    id: Mapped[int] = mapped_column(ForeignKey("sources.id"), primary_key=True)
    director: Mapped[str] = mapped_column()
    screenwriter: Mapped[Optional[str]] = mapped_column()
    cast: Mapped[Optional[List[str]]] = mapped_column(ARRAY(String))

    # helper func that makes obj print nicely
    def __repr__(self):
        return (f"<Movie(id={self.id}, title={self.title}, " 
                f"type={self.type}, release_date={self.release_date}, "
                f"franchise={self.franchise}, director={self.director}, "
                f"screenwriter={self.screenwriter}, cast={self.cast}, "
                f"genre={self.genre})>"
                )
