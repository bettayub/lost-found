"""rewards

Revision ID: 1899a500f6e5
Revises: d7acdceac47f
Create Date: 2023-11-01 13:00:56.593655

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1899a500f6e5'
down_revision = 'd7acdceac47f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.add_column(sa.Column('reward', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.drop_column('reward')

    # ### end Alembic commands ###