"""certification table change

Revision ID: dd62dc7da2a3
Revises: daed60513d3b
Create Date: 2022-01-19 16:53:19.242854

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "dd62dc7da2a3"
down_revision = "daed60513d3b"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("certification", sa.Column("issue_from", sa.String(), nullable=True))


def downgrade():
    op.drop_column("certification", "issue_from")
