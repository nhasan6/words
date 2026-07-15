"""move quote from source to word

Revision ID: d1c89c690c5f
Revises: ef28c1ceb8eb
Create Date: 2026-07-15 22:33:04.878302

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd1c89c690c5f'
down_revision: Union[str, Sequence[str], None] = 'ef28c1ceb8eb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('words', sa.Column('quote', sa.String(), nullable=True))
    op.drop_column('sources', 'quote')




def downgrade() -> None:
    """Downgrade schema."""
    op.add_column('sources', sa.Column('quote', sa.String(), nullable=True))
    op.drop_column('words', 'quote')
