"""Upgrate to python 3

Revision ID: 925c0962bca7
Revises: 1f0441aeca85
Create Date: 2020-02-19 11:06:29.520229

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = "925c0962bca7"
down_revision = "1f0441aeca85"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # op.create_table(
    #     "qstgroups",
    #     sa.Column("user_name", sa.String(length=80), nullable=False),
    #     sa.Column("qstgroups_id", sa.String(length=80), nullable=False),
    #     sa.Column("qstgroups_name", sa.String(length=120), nullable=True),
    #     sa.ForeignKeyConstraint(
    #         ["user_name"],
    #         ["user.user_name"],
    #         name=op.f("fk_qstgroups_user_name_user"),
    #         ondelete="CASCADE",
    #     ),
    #     sa.PrimaryKeyConstraint("user_name", "qstgroups_id", name=op.f("pk_qstgroups")),
    #     mysql_charset="utf8",
    #     mysql_engine="InnoDB",
    # )
    # op.add_column(
    #     "question", sa.Column("qstgroups_id", sa.String(length=80), nullable=True)
    # )
    # op.add_column(
    #     "question", sa.Column("qstgroups_user", sa.String(length=80), nullable=True)
    # )
    # op.add_column(
    #     "question",
    #     sa.Column(
    #         "question_visible",
    #         sa.Integer(),
    #         server_default=sa.text("'1'"),
    #         nullable=True,
    #     ),
    # )
    op.alter_column(
        "question",
        "question_dtype",
        existing_type=mysql.INTEGER(display_width=11),
        comment=None,
        existing_comment="Can also be Producer input, producer select, package select, enumerator select",
        existing_nullable=True,
    )
    op.alter_column(
        "question",
        "question_negstm",
        existing_type=mysql.VARCHAR(length=120),
        comment=None,
        existing_comment="Negative statement (if triad question)",
        existing_nullable=True,
    )
    op.alter_column(
        "question",
        "question_posstm",
        existing_type=mysql.VARCHAR(length=120),
        comment=None,
        existing_comment="Positive statement (if triad question)",
        existing_nullable=True,
    )
    # op.create_foreign_key(
    #     op.f("fk_question_qstgroups_user_qstgroups"),
    #     "question",
    #     "qstgroups",
    #     ["qstgroups_user", "qstgroups_id"],
    #     ["user_name", "qstgroups_id"],
    #     ondelete="CASCADE",
    # )
    op.drop_table_comment(
        "regsection",
        existing_comment="Registry section / Seccion en registro",
        schema=None,
    )
    op.drop_table_comment(
        "user", existing_comment="User table: Store the users", schema=None
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table_comment(
        "user", "User table: Store the users", existing_comment=None, schema=None
    )
    op.create_table_comment(
        "regsection",
        "Registry section / Seccion en registro",
        existing_comment=None,
        schema=None,
    )
    op.drop_constraint(
        op.f("fk_question_qstgroups_user_qstgroups"), "question", type_="foreignkey"
    )
    op.alter_column(
        "question",
        "question_posstm",
        existing_type=mysql.VARCHAR(length=120),
        comment="Positive statement (if triad question)",
        existing_nullable=True,
    )
    op.alter_column(
        "question",
        "question_negstm",
        existing_type=mysql.VARCHAR(length=120),
        comment="Negative statement (if triad question)",
        existing_nullable=True,
    )
    op.alter_column(
        "question",
        "question_dtype",
        existing_type=mysql.INTEGER(display_width=11),
        comment="Can also be Producer input, producer select, package select, enumerator select",
        existing_nullable=True,
    )
    op.drop_column("question", "question_visible")
    op.drop_column("question", "qstgroups_user")
    op.drop_column("question", "qstgroups_id")
    op.drop_table("qstgroups")
    # ### end Alembic commands ###
