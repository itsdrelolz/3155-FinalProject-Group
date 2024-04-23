"""Add token expiry to User model

Revision ID: 38cf4bdd548d
Revises: 26ad4e0b0b22
Create Date: 2024-04-22 21:40:07.091484

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '38cf4bdd548d'
down_revision = '26ad4e0b0b22'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('artist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('song',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('spotify_song_id', sa.String(length=22), nullable=False),
    sa.Column('num_streams', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('album',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('release_date', sa.Date(), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['artist.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('stream',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('spotify_song_id', sa.String(length=22), nullable=True),
    sa.Column('time', sa.Float(), nullable=False),
    sa.Column('user', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['song.id'], ),
    sa.ForeignKeyConstraint(['user'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('time')
    )
    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.alter_column('post_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('author_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('date_posted',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.alter_column('date_posted',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
        batch_op.alter_column('author_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('post_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    op.drop_table('stream')
    op.drop_table('album')
    op.drop_table('song')
    op.drop_table('artist')
    # ### end Alembic commands ###