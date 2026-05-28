from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import func
from datetime import datetime
from src.db.models.base import Base

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    # helper func that makes obj print nicely
    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email})>"