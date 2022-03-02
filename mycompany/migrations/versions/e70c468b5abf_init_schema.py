"""init schema

Revision ID: e70c468b5abf
Revises: 
Create Date: 2022-02-21 13:39:57.702102

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision = 'e70c468b5abf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
    CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
    """)

    op.execute("""
    CREATE OR REPLACE FUNCTION update_updated_at_column()
    RETURNS TRIGGER AS $$
    BEGIN
      NEW.updated_at = NOW();
      RETURN NEW;
    END;
    $$ language 'plpgsql';
    """)

    op.create_table(
        "departments",
        sa.Column(
            "id", UUID, primary_key=True, server_default=sa.func.uuid_generate_v1()
        ),
        sa.Column("name", sa.String, nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False, server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(), nullable=False, server_default=sa.func.now()),
    )

    op.execute("""
    CREATE TRIGGER departments_updated_at_trigger
    BEFORE UPDATE ON departments
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
    """)


def downgrade():
    op.execute("DROP TRIGGER IF EXISTS departments_updated_at_trigger ON departments;")
    op.drop_table("departments")
    op.execute("DROP FUNCTION IF EXISTS update_updated_at_column;")
