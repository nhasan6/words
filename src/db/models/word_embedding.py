

from datetime import datetime
from sqlalchemy import ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column
from pgvector.sqlalchemy import Vector
from src.db.models.base import Base


class WordEmbedding(Base):
    __tablename__ = "word_embeddings"
    word_id: Mapped[int] = mapped_column(ForeignKey("words.id"), primary_key=True)
    model: Mapped[str] = mapped_column(String, primary_key=True)
    embedding: Mapped[list[float]] = mapped_column(Vector(384))
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    # helper func that makes obj print nicely
    def __repr__(self):
        return f"<Embeddings(word_id={word_id}, embedding={self.embedding}, model={self.model})>"