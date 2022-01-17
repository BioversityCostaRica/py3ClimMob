"""climmobShare - Alter Schema - Unicode and Mediumtext

Revision ID: c6682ac905bc
Revises: 77d1b670f225
Create Date: 2021-10-22 10:45:22.019741

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = "c6682ac905bc"
down_revision = "77d1b670f225"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "activitylog",
        "log_message",
        existing_type=mysql.TEXT(),
        type_=mysql.MEDIUMTEXT(collation="utf8mb4_unicode_ci"),
        existing_nullable=True,
    )
    op.alter_column(
        "assessment",
        "extra",
        existing_type=mysql.TEXT(),
        type_=mysql.MEDIUMTEXT(collation="utf8mb4_unicode_ci"),
        existing_nullable=True,
    )
    op.alter_column(
        "asssection",
        "section_content",
        existing_type=mysql.TEXT(),
        type_=mysql.MEDIUMTEXT(collation="utf8mb4_unicode_ci"),
        existing_nullable=True,
    )
    op.alter_column(
        "i18n_asssection",
        "section_content",
        existing_type=mysql.TEXT(),
        type_=mysql.MEDIUMTEXT(collation="utf8mb4_unicode_ci"),
        existing_nullable=True,
    )
    op.alter_column(
        "i18n_project",
        "project_abstract",
        existing_type=mysql.TEXT(),
        type_=mysql.MEDIUMTEXT(collation="utf8mb4_unicode_ci"),
        existing_nullable=True,
    )
    op.alter_column(
        "i18n_question",
        "question_notes",
        existing_type=mysql.TEXT(),
        type_=mysql.MEDIUMTEXT(collation="utf8mb4_unicode_ci"),
        existing_nullable=True,
    )
    op.alter_column(
        "i18n_regsection",
        "section_content",
        existing_type=mysql.TEXT(),
        type_=mysql.MEDIUMTEXT(collation="utf8mb4_unicode_ci"),
        existing_nullable=True,
    )
    op.alter_column(
        "project",
        "extra",
        existing_type=mysql.TEXT(),
        type_=mysql.MEDIUMTEXT(collation="utf8mb4_unicode_ci"),
        existing_nullable=True,
    )
    op.alter_column(
        "project",
        "project_abstract",
        existing_type=mysql.TEXT(),
        type_=mysql.MEDIUMTEXT(collation="utf8mb4_unicode_ci"),
        existing_nullable=True,
    )
    op.alter_column(
        "project",
        "project_tags",
        existing_type=mysql.TEXT(),
        type_=mysql.MEDIUMTEXT(collation="utf8mb4_unicode_ci"),
        existing_nullable=True,
    )
    op.alter_column(
        "question",
        "extra",
        existing_type=mysql.TEXT(),
        type_=mysql.MEDIUMTEXT(collation="utf8mb4_unicode_ci"),
        existing_nullable=True,
    )
    op.alter_column(
        "question",
        "question_notes",
        existing_type=mysql.TEXT(),
        type_=mysql.MEDIUMTEXT(collation="utf8mb4_unicode_ci"),
        existing_nullable=True,
    )
    op.alter_column(
        "regsection",
        "section_content",
        existing_type=mysql.TEXT(),
        type_=mysql.MEDIUMTEXT(collation="utf8mb4_unicode_ci"),
        existing_nullable=True,
    )
    op.alter_column(
        "storageerrors",
        "command_executed",
        existing_type=mysql.TEXT(),
        type_=mysql.MEDIUMTEXT(collation="utf8mb4_unicode_ci"),
        existing_nullable=True,
    )
    op.alter_column(
        "storageerrors",
        "error_des",
        existing_type=mysql.TEXT(),
        type_=mysql.MEDIUMTEXT(collation="utf8mb4_unicode_ci"),
        existing_nullable=True,
    )
    op.alter_column(
        "user",
        "extra",
        existing_type=mysql.TEXT(),
        type_=mysql.MEDIUMTEXT(collation="utf8mb4_unicode_ci"),
        existing_nullable=True,
    )
    op.alter_column(
        "user",
        "user_about",
        existing_type=mysql.TEXT(),
        type_=mysql.MEDIUMTEXT(collation="utf8mb4_unicode_ci"),
        existing_nullable=True,
    )

    op.alter_column(
        "assesment_jsonlog",
        "json_file",
        existing_type=sa.UnicodeText(),
        type_=mysql.MEDIUMTEXT(collation="utf8mb4_unicode_ci"),
        existing_nullable=True,
    )
    op.alter_column(
        "assesment_jsonlog",
        "log_file",
        existing_type=sa.UnicodeText(),
        type_=mysql.MEDIUMTEXT(collation="utf8mb4_unicode_ci"),
        existing_nullable=True,
    )
    op.alter_column(
        "registry_jsonlog",
        "json_file",
        existing_type=sa.UnicodeText(),
        type_=mysql.MEDIUMTEXT(collation="utf8mb4_unicode_ci"),
        existing_nullable=True,
    )
    op.alter_column(
        "registry_jsonlog",
        "log_file",
        existing_type=sa.UnicodeText(),
        type_=mysql.MEDIUMTEXT(collation="utf8mb4_unicode_ci"),
        existing_nullable=True,
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "registry_jsonlog",
        "log_file",
        existing_type=mysql.MEDIUMTEXT(collation="utf8mb4_unicode_ci"),
        type_=sa.UnicodeText(),
        existing_nullable=True,
    )
    op.alter_column(
        "registry_jsonlog",
        "json_file",
        existing_type=mysql.MEDIUMTEXT(collation="utf8mb4_unicode_ci"),
        type_=sa.UnicodeText(),
        existing_nullable=True,
    )
    op.alter_column(
        "assesment_jsonlog",
        "log_file",
        existing_type=mysql.MEDIUMTEXT(collation="utf8mb4_unicode_ci"),
        type_=sa.UnicodeText(),
        existing_nullable=True,
    )
    op.alter_column(
        "assesment_jsonlog",
        "json_file",
        existing_type=mysql.MEDIUMTEXT(collation="utf8mb4_unicode_ci"),
        type_=sa.UnicodeText(),
        existing_nullable=True,
    )

    op.alter_column(
        "user",
        "user_about",
        existing_type=mysql.MEDIUMTEXT(collation="utf8mb4_unicode_ci"),
        type_=mysql.TEXT(),
        existing_nullable=True,
    )
    op.alter_column(
        "user",
        "extra",
        existing_type=mysql.MEDIUMTEXT(collation="utf8mb4_unicode_ci"),
        type_=mysql.TEXT(),
        existing_nullable=True,
    )
    op.alter_column(
        "storageerrors",
        "error_des",
        existing_type=mysql.MEDIUMTEXT(collation="utf8mb4_unicode_ci"),
        type_=mysql.TEXT(),
        existing_nullable=True,
    )
    op.alter_column(
        "storageerrors",
        "command_executed",
        existing_type=mysql.MEDIUMTEXT(collation="utf8mb4_unicode_ci"),
        type_=mysql.TEXT(),
        existing_nullable=True,
    )
    op.alter_column(
        "regsection",
        "section_content",
        existing_type=mysql.MEDIUMTEXT(collation="utf8mb4_unicode_ci"),
        type_=mysql.TEXT(),
        existing_nullable=True,
    )
    op.alter_column(
        "question",
        "question_notes",
        existing_type=mysql.MEDIUMTEXT(collation="utf8mb4_unicode_ci"),
        type_=mysql.TEXT(),
        existing_nullable=True,
    )
    op.alter_column(
        "question",
        "extra",
        existing_type=mysql.MEDIUMTEXT(collation="utf8mb4_unicode_ci"),
        type_=mysql.TEXT(),
        existing_nullable=True,
    )
    op.alter_column(
        "project",
        "project_tags",
        existing_type=mysql.MEDIUMTEXT(collation="utf8mb4_unicode_ci"),
        type_=mysql.TEXT(),
        existing_nullable=True,
    )
    op.alter_column(
        "project",
        "project_abstract",
        existing_type=mysql.MEDIUMTEXT(collation="utf8mb4_unicode_ci"),
        type_=mysql.TEXT(),
        existing_nullable=True,
    )
    op.alter_column(
        "project",
        "extra",
        existing_type=mysql.MEDIUMTEXT(collation="utf8mb4_unicode_ci"),
        type_=mysql.TEXT(),
        existing_nullable=True,
    )
    op.alter_column(
        "i18n_regsection",
        "section_content",
        existing_type=mysql.MEDIUMTEXT(collation="utf8mb4_unicode_ci"),
        type_=mysql.TEXT(),
        existing_nullable=True,
    )
    op.alter_column(
        "i18n_question",
        "question_notes",
        existing_type=mysql.MEDIUMTEXT(collation="utf8mb4_unicode_ci"),
        type_=mysql.TEXT(),
        existing_nullable=True,
    )
    op.alter_column(
        "i18n_project",
        "project_abstract",
        existing_type=mysql.MEDIUMTEXT(collation="utf8mb4_unicode_ci"),
        type_=mysql.TEXT(),
        existing_nullable=True,
    )
    op.alter_column(
        "i18n_asssection",
        "section_content",
        existing_type=mysql.MEDIUMTEXT(collation="utf8mb4_unicode_ci"),
        type_=mysql.TEXT(),
        existing_nullable=True,
    )
    op.alter_column(
        "asssection",
        "section_content",
        existing_type=mysql.MEDIUMTEXT(collation="utf8mb4_unicode_ci"),
        type_=mysql.TEXT(),
        existing_nullable=True,
    )
    op.alter_column(
        "assessment",
        "extra",
        existing_type=mysql.MEDIUMTEXT(collation="utf8mb4_unicode_ci"),
        type_=mysql.TEXT(),
        existing_nullable=True,
    )
    op.alter_column(
        "activitylog",
        "log_message",
        existing_type=mysql.MEDIUMTEXT(collation="utf8mb4_unicode_ci"),
        type_=mysql.TEXT(),
        existing_nullable=True,
    )
    # ### end Alembic commands ###
