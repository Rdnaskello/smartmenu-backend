from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'aa18c75da981'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        "meals",
        sa.Column("id", sa.Integer(), primary_key=True, index=True),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("category", sa.String(), nullable=False),
        sa.Column("ingredients", sa.String(), nullable=False)
    )

def downgrade():
    op.drop_table("meals")
