"""empty message

Revision ID: 2daa4f587028
Revises: 3e65332c45d5
Create Date: 2025-04-07 00:48:28.580621

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2daa4f587028'
down_revision = '3e65332c45d5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('grievance', schema=None) as batch_op:
        batch_op.alter_column('audio',
               existing_type=mysql.VARCHAR(length=200),
               type_=sa.LargeBinary(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('grievance', schema=None) as batch_op:
        batch_op.alter_column('audio',
               existing_type=sa.LargeBinary(),
               type_=mysql.VARCHAR(length=200),
               existing_nullable=True)

    # ### end Alembic commands ###
