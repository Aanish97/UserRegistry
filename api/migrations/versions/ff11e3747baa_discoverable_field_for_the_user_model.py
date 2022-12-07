"""Discoverable field for the User model

Revision ID: ff11e3747baa
Revises: dca61b200960
Create Date: 2022-12-07 09:19:01.044281

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ff11e3747baa'
down_revision = 'dca61b200960'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('discoverable', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('discoverable')

    # ### end Alembic commands ###