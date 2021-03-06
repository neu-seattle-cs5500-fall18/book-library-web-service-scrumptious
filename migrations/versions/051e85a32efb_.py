"""empty message

Revision ID: 051e85a32efb
Revises: a6ce3ddca8e6
Create Date: 2018-12-12 15:59:00.652807

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '051e85a32efb'
down_revision = 'a6ce3ddca8e6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('book_collection', 'is_deleted')
    op.create_foreign_key(None, 'checkout', 'user', ['user_id'], ['user_id'])
    op.alter_column('collections', 'book_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_constraint('user_user_first_name_user_last_name_email_key', 'user', type_='unique')
    op.create_unique_constraint(None, 'user', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.create_unique_constraint('user_user_first_name_user_last_name_email_key', 'user', ['user_first_name', 'user_last_name', 'email'])
    op.alter_column('collections', 'book_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_constraint(None, 'checkout', type_='foreignkey')
    op.add_column('book_collection', sa.Column('is_deleted', sa.BOOLEAN(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
