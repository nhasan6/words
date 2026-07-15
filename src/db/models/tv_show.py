from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from src.db.models.source import Source, SourceType

class TvShow(Source):
    __tablename__ = "tv_shows"
    __mapper_args__ = {
        "polymorphic_identity": SourceType.tv_show
    }
    # Database level: foreign key column pointing to sources.id
    id: Mapped[int] = mapped_column(ForeignKey("sources.id"), primary_key=True)
    franchise: Mapped[Optional[str]] = mapped_column()
    episode_number: Mapped[int] = mapped_column()
    season_number: Mapped[int] = mapped_column()
    director: Mapped[Optional[str]] = mapped_column()
    screenwriter: Mapped[Optional[str]] = mapped_column()
    actor: Mapped[str] = mapped_column()
    character: Mapped[Optional[str]] = mapped_column()

    # helper func that makes obj print nicely
    def __repr__(self):
        return (f"<TV Show(id={self.id}, title={self.title}, " 
                f"type={self.type}, release_date={self.release_date}, "
                f"franchise={self.franchise}, S{self.season_number}E{self.episode_number}, director={self.director}, "
                f"screenwriter={self.screenwriter}, actor={self.actor}, "
                f"character={self.character}, genre={self.genre})>"
                )
