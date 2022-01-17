"""climmobShare - I18nProyect - Remove user_name and project_cod

Revision ID: 48ae99a5674b
Revises: 0ad2b87a9cc0
Create Date: 2021-08-18 14:58:54.610876

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = "48ae99a5674b"
down_revision = "0ad2b87a9cc0"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("i18n_project", "project_cod")
    op.drop_column("i18n_project", "user_name")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "i18n_project", sa.Column("user_name", mysql.VARCHAR(length=80), nullable=False)
    )
    op.add_column(
        "i18n_project",
        sa.Column("project_cod", mysql.VARCHAR(length=80), nullable=False),
    )
    # ### end Alembic commands ###
