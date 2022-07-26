"""empty message

Revision ID: d470ba038fe2
Revises: 035289a9fb4c
Create Date: 2022-07-23 23:49:48.154378

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'd470ba038fe2'
down_revision = '035289a9fb4c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('address', sa.Column('patient_id', postgresql.UUID(as_uuid=True), nullable=True))
    op.add_column('address', sa.Column('country', sa.String(length=60), nullable=False))
    op.add_column('address', sa.Column('address', sa.Text(), nullable=False))
    op.add_column('address', sa.Column('city', sa.String(length=60), nullable=False))
    op.add_column('address', sa.Column('zip_code', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'address', 'patient', ['patient_id'], ['id'])
    op.add_column('patient', sa.Column('address_id', postgresql.UUID(as_uuid=True), nullable=True))
    op.create_foreign_key(None, 'patient', 'address', ['address_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'patient', type_='foreignkey')
    op.drop_column('patient', 'address_id')
    op.drop_constraint(None, 'address', type_='foreignkey')
    op.drop_column('address', 'zip_code')
    op.drop_column('address', 'city')
    op.drop_column('address', 'address')
    op.drop_column('address', 'country')
    op.drop_column('address', 'patient_id')
    # ### end Alembic commands ###
