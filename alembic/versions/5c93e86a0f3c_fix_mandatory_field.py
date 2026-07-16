"""fix mandatory field

Revision ID: 5c93e86a0f3c
Revises: cfc22ae6f8c1
Create Date: 2026-07-16 04:00:17.108652

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5c93e86a0f3c'
down_revision: Union[str, Sequence[str], None] = 'cfc22ae6f8c1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column('sources', 'release_date', nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column('sources', 'release_date', nullable=False)
    # ### end Alembic commands ###