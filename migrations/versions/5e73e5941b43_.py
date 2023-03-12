"""empty message

Revision ID: 5e73e5941b43
Revises: 69e64d45232c
Create Date: 2023-03-12 14:04:07.808007

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e73e5941b43'
down_revision = '69e64d45232c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('property_profiles', schema=None) as batch_op:
        batch_op.alter_column('desc',
               existing_type=sa.VARCHAR(length=180),
               type_=sa.String(length=250),
               existing_nullable=True)
        batch_op.alter_column('price',
               existing_type=sa.VARCHAR(length=180),
               type_=sa.String(length=80),
               existing_nullable=True)
        batch_op.alter_column('photo_filename',
               existing_type=sa.VARCHAR(length=180),
               type_=sa.String(length=80),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('property_profiles', schema=None) as batch_op:
        batch_op.alter_column('photo_filename',
               existing_type=sa.String(length=80),
               type_=sa.VARCHAR(length=180),
               existing_nullable=True)
        batch_op.alter_column('price',
               existing_type=sa.String(length=80),
               type_=sa.VARCHAR(length=180),
               existing_nullable=True)
        batch_op.alter_column('desc',
               existing_type=sa.String(length=250),
               type_=sa.VARCHAR(length=180),
               existing_nullable=True)

    # ### end Alembic commands ###
