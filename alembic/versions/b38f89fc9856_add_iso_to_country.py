"""add iso to country

Revision ID: b38f89fc9856
Revises: f079cff96943
Create Date: 2020-03-26 18:50:32.815043

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b38f89fc9856'
down_revision = 'f079cff96943'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('country', sa.Column('cnty_iso', sa.String(length=3), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('country', 'cnty_iso')
    # ### end Alembic commands ###