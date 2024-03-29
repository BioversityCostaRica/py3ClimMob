"""Add field user_last_login to user

Revision ID: 0202a70622fb
Revises: ae0b4d44b5a1
Create Date: 2023-02-28 11:27:47.528233

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = "0202a70622fb"
down_revision = "ae0b4d44b5a1"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("user", sa.Column("user_last_login", sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("user", "user_last_login")
    # ### end Alembic commands ###
