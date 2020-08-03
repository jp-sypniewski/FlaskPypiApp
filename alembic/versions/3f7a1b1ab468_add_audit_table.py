"""add audit table

Revision ID: 3f7a1b1ab468
Revises: 7e12373361b7
Create Date: 2020-08-03 14:53:11.090210

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f7a1b1ab468'
down_revision = '7e12373361b7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('auditing',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_auditing_created_date'), 'auditing', ['created_date'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_auditing_created_date'), table_name='auditing')
    op.drop_table('auditing')
    # ### end Alembic commands ###
