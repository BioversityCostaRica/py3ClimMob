"""Create table i18n_user

Revision ID: e3dd7e27aa2e
Revises: cc47b176974c
Create Date: 2023-04-13 10:40:45.003358

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = "e3dd7e27aa2e"
down_revision = "cc47b176974c"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "i18n_user",
        sa.Column("lang_code", sa.Unicode(length=5), nullable=False),
        sa.Column("user_name", sa.Unicode(length=80), nullable=False),
        sa.Column(
            "lang_default", sa.Integer(), server_default=sa.text("'0'"), nullable=True
        ),
        sa.ForeignKeyConstraint(
            ["lang_code"], ["i18n.lang_code"], name=op.f("fk_i18n_user_lang_code_i18n")
        ),
        sa.ForeignKeyConstraint(
            ["user_name"], ["user.user_name"], name=op.f("fk_i18n_user_user_name_user")
        ),
        sa.PrimaryKeyConstraint("lang_code", "user_name", name=op.f("pk_i18n_user")),
        mysql_charset="utf8mb4",
        mysql_engine="InnoDB",
        mysql_collate="utf8mb4_unicode_ci",
    )
    op.create_index(
        op.f("ix_i18n_user_lang_code"), "i18n_user", ["lang_code"], unique=False
    )
    op.create_index(
        op.f("ix_i18n_user_user_name"), "i18n_user", ["user_name"], unique=False
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_i18n_user_user_name"), table_name="i18n_user")
    op.drop_index(op.f("ix_i18n_user_lang_code"), table_name="i18n_user")
    op.drop_table("i18n_user")
    # ### end Alembic commands ###
