"""Add is_deleted mixin

Revision ID: f7cb35c73cd8
Revises: 4041e1f3b0a9
Create Date: 2023-05-20 12:57:36.927490

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f7cb35c73cd8'
down_revision = '4041e1f3b0a9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('categories', sa.Column('is_deleted', sa.Boolean(), nullable=False))
    op.add_column('products', sa.Column('is_deleted', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('products', 'is_deleted')
    op.drop_column('categories', 'is_deleted')
    # ### end Alembic commands ###
