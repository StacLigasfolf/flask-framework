from alembic import op
import sqlalchemy as sa

revision = 'c9bf094d20f2'
down_revision = '0fe354147ed7'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('tags',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=255), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('article_tag_association',
                    sa.Column('article_id', sa.Integer(), nullable=False),
                    sa.Column('tag_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['article_id'], ['articles.id'], ),
                    sa.ForeignKeyConstraint(['tag_id'], ['tags.id'], )
                    )
    op.create_unique_constraint(None, 'users', ['email'])


def downgrade():
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_table('article_tag_association')
    op.drop_table('tags')
