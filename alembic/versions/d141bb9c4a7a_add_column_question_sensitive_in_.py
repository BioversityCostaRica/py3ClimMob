"""add column question_sensitive in question table

Revision ID: d141bb9c4a7a
Revises: 55702fd698f4
Create Date: 2023-04-11 17:05:55.783552

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = "d141bb9c4a7a"
down_revision = "55702fd698f4"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "question",
        sa.Column(
            "question_sensitive",
            sa.Integer(),
            server_default=sa.text("'0'"),
            nullable=True,
        ),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("question", "question_sensitive")
    # ### end Alembic commands ###
