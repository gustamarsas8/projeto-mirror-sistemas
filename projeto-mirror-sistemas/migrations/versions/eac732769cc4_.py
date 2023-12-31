"""empty message

Revision ID: eac732769cc4
Revises: 3258dc309c9a
Create Date: 2023-07-26 09:36:40.845791

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eac732769cc4'
down_revision = '3258dc309c9a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pedidos', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('produto_id')

    with op.batch_alter_table('produtos', schema=None) as batch_op:
        batch_op.add_column(sa.Column('pedido_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_produto_pedido_id', 'pedidos', ['pedido_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('produtos', schema=None) as batch_op:
        batch_op.drop_constraint('fk_produto_pedido_id', type_='foreignkey')
        batch_op.drop_column('pedido_id')

    with op.batch_alter_table('pedidos', schema=None) as batch_op:
        batch_op.add_column(sa.Column('produto_id', sa.INTEGER(), nullable=False))
        batch_op.create_foreign_key(None, 'produtos', ['produto_id'], ['id'])

    # ### end Alembic commands ###
