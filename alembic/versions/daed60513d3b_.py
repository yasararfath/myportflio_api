"""empty message

Revision ID: daed60513d3b
Revises: 53603601b026
Create Date: 2022-01-14 00:37:54.922088

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "daed60513d3b"
down_revision = "53603601b026"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("about", 
    sa.Column("wesbite",sa.String(),nullable=True))


def downgrade():
    op.drop_column("about", "website")
