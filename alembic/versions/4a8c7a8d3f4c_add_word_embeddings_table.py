"""add word embeddings table

Revision ID: 4a8c7a8d3f4c
Revises: 9f51f3814d75
Create Date: 2026-07-29 18:10:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from pgvector.sqlalchemy import Vector


# revision identifiers, used by Alembic.
revision: str = "4a8c7a8d3f4c"
down_revision: Union[str, Sequence[str], None] = "9f51f3814d75"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("CREATE EXTENSION IF NOT EXISTS vector")
    op.create_table(
        "word_embeddings",
        sa.Column("word_id", sa.Integer(), nullable=False),
        sa.Column("model", sa.String(), nullable=False),
        sa.Column("embedding", Vector(384), nullable=True),
        sa.Column("created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=True),
        sa.ForeignKeyConstraint(["word_id"], ["words.id"], name=op.f("fk_word_embeddings_word_id_words")),
        sa.PrimaryKeyConstraint("word_id", "model", name=op.f("pk_word_embeddings")),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("word_embeddings")
