from alembic import op
import sqlalchemy as sa

revision = 'ba574593435e'
down_revision = 'c9bf094d20f2'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('is_staff', sa.Boolean(), nullable=True))
    op.create_unique_constraint(None, 'users', ['email'])


def downgrade():
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('users', 'is_staff')
