"""climmobShare - Prjalia - table relationship

Revision ID: 1827cbfc4260
Revises: fef7f1677035
Create Date: 2021-08-10 11:40:03.844477

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "1827cbfc4260"
down_revision = "fef7f1677035"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("PRIMARY", "prjalias", type_="primary")
    op.create_primary_key(
        "pk_prjalias", "prjalias", ["project_id", "tech_id", "alias_id"]
    )

    op.create_index(
        "fk_prjalias_prjtech1_idx", "prjalias", ["project_id", "tech_id"], unique=False
    )
    op.create_index(
        "fk_prjalias_techalias1_idx",
        "prjalias",
        ["tech_used", "alias_used"],
        unique=False,
    )
    op.create_foreign_key(
        op.f("fk_prjalias_tech_used_techalias"),
        "prjalias",
        "techalias",
        ["tech_used", "alias_used"],
        ["tech_id", "alias_id"],
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        op.f("fk_prjalias_project_id_prjtech"),
        "prjalias",
        "prjtech",
        ["project_id", "tech_id"],
        ["project_id", "tech_id"],
        ondelete="CASCADE",
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("PRIMARY", "prjalias", type_="primary")
    op.create_primary_key(
        "pk_prjalias", "prjalias", ["user_name", "project_cod", "tech_id", "alias_id"]
    )

    op.drop_constraint(
        op.f("fk_prjalias_project_id_prjtech"), "prjalias", type_="foreignkey"
    )
    op.drop_constraint(
        op.f("fk_prjalias_tech_used_techalias"), "prjalias", type_="foreignkey"
    )
    op.drop_index("fk_prjalias_techalias1_idx", table_name="prjalias")
    op.drop_index("fk_prjalias_prjtech1_idx", table_name="prjalias")
    # ### end Alembic commands ###