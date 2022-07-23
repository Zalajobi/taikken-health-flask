"""empty message

Revision ID: 8f1491c8dfa4
Revises: 6beb2581ad40
Create Date: 2022-07-23 23:47:54.742822

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '8f1491c8dfa4'
down_revision = '6beb2581ad40'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('patient', sa.Column('registration_id', postgresql.UUID(as_uuid=True), nullable=True))
    op.create_foreign_key(None, 'patient', 'registration', ['registration_id'], ['id'])
    op.add_column('registration', sa.Column('name', sa.String(), nullable=False))
    op.add_column('registration', sa.Column('description', sa.Text(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('registration', 'description')
    op.drop_column('registration', 'name')
    op.drop_constraint(None, 'patient', type_='foreignkey')
    op.drop_column('patient', 'registration_id')
    # ### end Alembic commands ###