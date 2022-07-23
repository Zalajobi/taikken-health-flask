"""empty message

Revision ID: 79ed5cbaf618
Revises: cc1f90f452f4
Create Date: 2022-07-23 23:53:53.336578

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '79ed5cbaf618'
down_revision = 'cc1f90f452f4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('provider', sa.Column('role_id', postgresql.UUID(as_uuid=True), nullable=True))
    op.create_foreign_key(None, 'provider', 'role', ['role_id'], ['id'])
    op.add_column('role', sa.Column('name', sa.String(), nullable=False))
    op.add_column('role', sa.Column('description', sa.Text(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('role', 'description')
    op.drop_column('role', 'name')
    op.drop_constraint(None, 'provider', type_='foreignkey')
    op.drop_column('provider', 'role_id')
    # ### end Alembic commands ###
