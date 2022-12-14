"""empty message

Revision ID: d207109a59b5
Revises: 3d03f81fc641
Create Date: 2022-11-03 16:40:12.965298

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd207109a59b5'
down_revision = '3d03f81fc641'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('country',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('code', sa.Integer(), nullable=True),
    sa.Column('population', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('country')
    # ### end Alembic commands ###
