"""empty message

Revision ID: 356212bd1b3d
Revises: 292684371935
Create Date: 2022-09-04 13:30:13.721238

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '356212bd1b3d'
down_revision = '292684371935'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('tax', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('products', 'tax')
    # ### end Alembic commands ###
