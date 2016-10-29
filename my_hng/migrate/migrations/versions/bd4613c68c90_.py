"""empty message

Revision ID: bd4613c68c90
Revises: 
Create Date: 2016-06-20 03:47:50.609466

"""

# revision identifiers, used by Alembic.
revision = 'bd4613c68c90'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###


def downgrade_():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###


def upgrade_myhngn5_admin():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('article',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('published_date', sa.Date(), nullable=True),
    sa.Column('added_date', sa.Date(), nullable=True),
    sa.Column('title', sa.String(length=500), nullable=True),
    sa.Column('category', sa.String(length=100), nullable=True),
    sa.Column('summary', sa.String(length=500), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('author_id', sa.String(length=50), nullable=True),
    sa.Column('status', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('id')
    )
    ### end Alembic commands ###


def downgrade_myhngn5_admin():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('article')
    ### end Alembic commands ###
