"""change db model

Revision ID: 2cf9174542d2
Revises: 
Create Date: 2024-03-24 21:22:43.328260

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2cf9174542d2'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'shelves',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('shelve', sa.String(50), nullable=False),
    )
    op.create_table(
        'good_shelve',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('good_id', sa.Integer, sa.ForeignKey('goods.id', onupdate="CASCADE", ondelete="CASCADE")),
        sa.Column('shelve_id', sa.Integer, sa.ForeignKey('shelves.id', onupdate="CASCADE", ondelete="CASCADE")),
        sa.Column('is_main', sa.Boolean, nullable=False),
    )


def downgrade() -> None:
    op.drop_table('minor_shelves')
    op.drop_table('main_shelves')
