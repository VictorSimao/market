"""empty message

Revision ID: 5c3db6508a0e
Revises: 
Create Date: 2021-02-19 17:05:36.559912

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5c3db6508a0e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('salesman',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('fantasy_name', sa.String(length=80), nullable=False),
    sa.Column('company_name', sa.String(length=80), nullable=False),
    sa.Column('cnpj', sa.String(length=36), nullable=False),
    sa.Column('email', sa.String(length=80), nullable=False),
    sa.Column('phone', sa.String(length=36), nullable=False),
    sa.Column('address', sa.String(length=240), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('salesman')
    # ### end Alembic commands ###