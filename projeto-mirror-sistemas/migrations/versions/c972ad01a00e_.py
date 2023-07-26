"""empty message

Revision ID: c972ad01a00e
Revises: 3f29d21e7392
Create Date: 2023-07-26 09:33:02.923588

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c972ad01a00e'
down_revision = '3f29d21e7392'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pedidos', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('produto_id')

    with op.batch_alter_table('produtos', schema=None) as batch_op:
        batch_op.add_column(sa.Column('pedido_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'pedidos', ['pedido_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('produtos', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('pedido_id')

    with op.batch_alter_table('pedidos', schema=None) as batch_op:
        batch_op.add_column(sa.Column('produto_id', sa.INTEGER(), nullable=False))
        batch_op.create_foreign_key(None, 'produtos', ['produto_id'], ['id'])

    # ### end Alembic commands ###
