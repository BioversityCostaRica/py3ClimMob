"""climmobShare - Prjalia - add project_id

Revision ID: 067043357453
Revises: 26532fdba4b6
Create Date: 2021-08-03 13:46:28.739698

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.orm.session import Session
from climmob.models.climmobv4 import Prjalia, Project

# revision identifiers, used by Alembic.
revision = "067043357453"
down_revision = "26532fdba4b6"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "prjalias", sa.Column("project_id", sa.Unicode(length=64), nullable=True)
    )

    session = Session(bind=op.get_bind())
    try:
        projects = session.execute("Select * from project")
        for project in projects:
            session.execute(
                "UPDATE prjalias SET project_id = '"
                + project.project_id
                + "' WHERE (user_name = '"
                + project.user_name
                + "') and (project_cod = '"
                + project.project_cod
                + "');"
            )
    except Exception as e:
        print(str(e))
        exit(1)

    session.commit()
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("prjalias", "project_id")
    # ### end Alembic commands ###