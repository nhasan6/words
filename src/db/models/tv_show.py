from typing import List, Optional
from sqlalchemy import ARRAY, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column
from src.db.models.source import Source, SourceType

class TvShow(Source):
    __tablename__ = "tv_shows"
    __mapper_args__ = {
        "polymorphic_identity": SourceType.tv_show
    }
    # Database level: foreign key column pointing to sources.id
    id: Mapped[int] = mapped_column(ForeignKey("sources.id"), primary_key=True)
    episode_number: Mapped[int] = mapped_column()
    season_number: Mapped[int] = mapped_column()
    director: Mapped[Optional[str]] = mapped_column()
    screenwriter: Mapped[Optional[str]] = mapped_column()
    cast: Mapped[Optional[List[str]]] = mapped_column(ARRAY(String))

    # helper func that makes obj print nicely
    def __repr__(self):
        return (f"<TV Show(id={self.id}, title={self.title}, " 
                f"type={self.type}, release_date={self.release_date}, "
                f"franchise={self.franchise}, S{self.season_number}E{self.episode_number}, director={self.director}, "
                f"screenwriter={self.screenwriter}, cast={self.cast}, "
                f"genre={self.genre})>"
                )
