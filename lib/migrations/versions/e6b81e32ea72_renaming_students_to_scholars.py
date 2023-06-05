"""Renaming students to scholars

Revision ID: e6b81e32ea72
Revises: 791279dd0760
Create Date: 2023-06-05 19:40:19.620267

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e6b81e32ea72'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')



def downgrade() -> None:
    op.rename_table('scholars', 'students')
