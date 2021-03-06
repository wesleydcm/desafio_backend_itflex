"""empty message

Revision ID: db3d850bc3cd
Revises: 
Create Date: 2021-10-12 15:32:03.511756

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dfc21a0578d6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('certificates',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.VARCHAR(length=30), nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('expiration', sa.Integer(), nullable=False),
    sa.Column('expirated_at', sa.DateTime(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('groups',
    sa.Column('group_id', sa.Integer(), nullable=False),
    sa.Column('code', sa.Integer(), nullable=False),
    sa.Column('group_name', sa.VARCHAR(length=30), nullable=False),
    sa.PrimaryKeyConstraint('group_id'),
    sa.UniqueConstraint('code'),
    sa.UniqueConstraint('group_name')
    )
    op.create_table('certificates_groups',
    sa.Column('certificate_group_id', sa.Integer(), nullable=False),
    sa.Column('certificate_id', sa.Integer(), nullable=True),
    sa.Column('group_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['certificate_id'], ['certificates.id'], ),
    sa.ForeignKeyConstraint(['group_id'], ['groups.group_id'], ),
    sa.PrimaryKeyConstraint('certificate_group_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('certificates_groups')
    op.drop_table('groups')
    op.drop_table('certificates')
    # ### end Alembic commands ###
