"""add field question_perfstmt to table i18n_question

Revision ID: 5e36aa1453be
Revises: 705ed01f1cd6
Create Date: 2021-06-04 12:13:12.021164

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "5e36aa1453be"
down_revision = "705ed01f1cd6"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "i18n_question",
        sa.Column("question_perfstmt", sa.String(length=120), nullable=True),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("i18n_question", "question_perfstmt")
    # ### end Alembic commands ###
