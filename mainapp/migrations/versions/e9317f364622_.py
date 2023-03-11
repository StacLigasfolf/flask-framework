from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e9317f364622'
down_revision = '2f15772923f5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('first_name', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('last_name', sa.String(length=255), nullable=True))
    op.drop_column('users', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('name', sa.VARCHAR(length=255), nullable=True))
    op.drop_column('users', 'last_name')
    op.drop_column('users', 'first_name')
    # ### end Alembic commands ###