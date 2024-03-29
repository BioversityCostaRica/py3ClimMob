"""Inserts and updates required for ClimMob questions

Revision ID: 23d2f8154412
Revises: a6eba1db4488
Create Date: 2023-07-19 15:16:05.252702

"""
from alembic import op
from sqlalchemy import String, Integer
from sqlalchemy.sql import table, column
from sqlalchemy.orm.session import Session

# revision identifiers, used by Alembic.
revision = "23d2f8154412"
down_revision = "a6eba1db4488"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    i18n_question_inserts = [
        {
            "question_id": 162,
            "lang_code": "es",
            "question_desc": "Código de paquete",
            "question_name": "Código de paquete",
        },
        {
            "question_id": 163,
            "lang_code": "es",
            "question_desc": "Seleccione un participante",
            "question_name": "Seleccione un participante",
        },
        {
            "question_id": 199,
            "lang_code": "es",
            "question_desc": "Nombre del participante",
            "question_name": "Nombre del participante",
        },
        {
            "question_id": 162,
            "lang_code": "fr",
            "question_desc": "Code du paquet",
            "question_name": "Code du paquet",
        },
        {
            "question_id": 163,
            "lang_code": "fr",
            "question_desc": "Sélectionnez un participant",
            "question_name": "Sélectionnez un participant",
        },
        {
            "question_id": 199,
            "lang_code": "fr",
            "question_desc": "Nom du participant",
            "question_name": "Nom du participant",
        },
    ]

    i18n_question = table(
        "i18n_question",
        column("question_id", Integer),
        column("lang_code", String),
        column("question_desc", String),
        column("question_name", String),
    )
    try:
        op.bulk_insert(i18n_question, i18n_question_inserts)
    except:
        pass

    i18n_user_inserts = [
        {"lang_code": "en", "user_name": "bioversity", "lang_default": 1},
        {"lang_code": "es", "user_name": "bioversity", "lang_default": 0},
        {"lang_code": "fr", "user_name": "bioversity", "lang_default": 0},
    ]

    i18n_user = table(
        "i18n_user",
        column("lang_code", String),
        column("user_name", String),
        column("lang_default", Integer),
    )
    try:
        op.bulk_insert(i18n_user, i18n_user_inserts)
    except:
        pass

    session = Session(bind=op.get_bind())
    conn = op.get_bind()

    try:
        conn.execute(
            "UPDATE question SET question_lang = 'en' WHERE (question_id = '162')"
        )
        conn.execute(
            "UPDATE question SET question_lang = 'en' WHERE (question_id = '163')"
        )
        conn.execute(
            "UPDATE question SET question_lang = 'en' WHERE (question_id = '199')"
        )

    except Exception as e:
        print(str(e))
        exit(1)

    session.commit()

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    print("")
    # ### end Alembic commands ###
