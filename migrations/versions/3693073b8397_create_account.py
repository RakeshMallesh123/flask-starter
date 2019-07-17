"""Create Account

Revision ID: 3693073b8397
Revises: 3a9f65801ff9
Create Date: 2019-07-17 14:48:35.268155

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import DateTime


# revision identifiers, used by Alembic.
revision = '3693073b8397'
down_revision = '3a9f65801ff9'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'accounts',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('firstname', sa.Unicode(50), nullable=False),
        sa.Column('lastname', sa.Unicode(50), nullable=False),
        sa.Column('email', sa.Unicode(100)),
        sa.Column('password', sa.Unicode(200)),
        sa.Column('role', sa.Unicode(200)),
        sa.Column('created_at', DateTime(timezone=True)),
        sa.Column('updated_at', DateTime(timezone=True)),
        sa.Column('deleted_at', DateTime(timezone=True)),
    )


def downgrade():
    op.drop_table('accounts')
