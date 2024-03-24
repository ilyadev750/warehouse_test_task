"""add constraint

Revision ID: 99d9d6f04c4c
Revises: 2cf9174542d2
Create Date: 2024-03-24 22:08:30.274390

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '99d9d6f04c4c'
down_revision: Union[str, None] = '2cf9174542d2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_unique_constraint('unique_row', 'good_shelve', ['good_id', 'shelve_id', 'is_main'], schema='public')


def downgrade() -> None:
    pass
