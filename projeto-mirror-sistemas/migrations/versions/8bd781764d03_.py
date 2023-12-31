"""empty message

Revision ID: 8bd781764d03
Revises: 51e92870ce4e
Create Date: 2023-07-25 11:38:23.484205

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8bd781764d03'
down_revision = '51e92870ce4e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pedidos', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('produto_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pedidos', schema=None) as batch_op:
        batch_op.add_column(sa.Column('produto_id', sa.INTEGER(), nullable=False))
        batch_op.create_foreign_key(None, 'produtos', ['produto_id'], ['id'])

    # ### end Alembic commands ###
