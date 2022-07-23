"""empty message

Revision ID: 80d88346e202
Revises: a5ce826a63dc
Create Date: 2022-07-23 23:50:38.095180

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '80d88346e202'
down_revision = 'a5ce826a63dc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('allergy', sa.Column('patient_id', postgresql.UUID(as_uuid=True), nullable=True))
    op.add_column('allergy', sa.Column('name', sa.String(), nullable=False))
    op.add_column('allergy', sa.Column('description', sa.Text(), nullable=False))
    op.create_foreign_key(None, 'allergy', 'patient', ['patient_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'allergy', type_='foreignkey')
    op.drop_column('allergy', 'description')
    op.drop_column('allergy', 'name')
    op.drop_column('allergy', 'patient_id')
    # ### end Alembic commands ###