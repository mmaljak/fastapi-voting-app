"""Add foreign key to posts table

Revision ID: fe398d95c618
Revises: 1de782e02b8c
Create Date: 2024-09-26 16:51:00.713179

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

#### CONTINUE FROM 11:13:30 h


# revision identifiers, used by Alembic.
revision: str = 'fe398d95c618'
down_revision: Union[str, None] = '1de782e02b8c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer, nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", 
                          local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
