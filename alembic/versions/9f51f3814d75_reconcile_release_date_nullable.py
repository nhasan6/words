"""reconcile release_date nullability

Revision ID: 9f51f3814d75
Revises: 5c93e86a0f3c
Create Date: 2026-07-29 17:37:36.011209

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9f51f3814d75'
down_revision: Union[str, Sequence[str], None] = '5c93e86a0f3c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # The database already allows null values for release_date.
    # Keep this migration as a no-op so the revision chain can advance.
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
