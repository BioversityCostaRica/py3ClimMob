"""Update table Enumerator add field enum_telephone

Revision ID: 0176d2461013
Revises: 27d21076ce46
Create Date: 2022-04-05 14:47:16.382887

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "0176d2461013"
down_revision = "27d21076ce46"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "enumerator",
        sa.Column(
            "enum_telephone",
            sa.Unicode(length=120),
            server_default=sa.text("''"),
            nullable=True,
        ),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("enumerator", "enum_telephone")
    # ### end Alembic commands ###
