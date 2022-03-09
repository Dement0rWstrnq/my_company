"""update schema

Revision ID: ff97ba0063d5
Revises: e70c468b5abf
Create Date: 2022-02-21 14:18:29.665813

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision = "ff97ba0063d5"
down_revision = "e70c468b5abf"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "positions",
        sa.Column(
            "id", UUID, primary_key=True, server_default=sa.func.uuid_generate_v1()
        ),
        sa.Column("name", sa.String, nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), nullable=False, server_default=sa.func.now()
        ),
        sa.Column(
            "updated_at", sa.DateTime(), nullable=False, server_default=sa.func.now()
        ),
    )

    op.execute(
        """
    CREATE TRIGGER positions_updated_at_trigger
    BEFORE UPDATE ON positions
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
    """
    )

    op.create_table(
        "workers",
        sa.Column(
            "id", UUID, primary_key=True, server_default=sa.func.uuid_generate_v1()
        ),
        sa.Column("name", sa.String, nullable=False),
        sa.Column("surname", sa.String, nullable=False),
        sa.Column(
            "department_id",
            UUID,
            ForeignKey("departments.id", ondelete="CASCADE", onupdate="CASCADE"),
            nullable=False,
        ),
        sa.Column(
            "position_id",
            UUID,
            ForeignKey("positions.id", ondelete="CASCADE", onupdate="CASCADE"),
            nullable=False,
        ),
        sa.Column(
            "created_at", sa.DateTime(), nullable=False, server_default=sa.func.now()
        ),
        sa.Column(
            "updated_at", sa.DateTime(), nullable=False, server_default=sa.func.now()
        ),
    )

    op.execute(
        """
    CREATE TRIGGER workers_updated_at_trigger
    BEFORE UPDATE ON workers
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
    """
    )

    op.create_table(
        "skills",
        sa.Column(
            "id",
            UUID,
            primary_key=True,
            server_default=sa.func.uuid_generate_v1(),
            nullable=False,
        ),
        sa.Column("name", sa.String, nullable=False),
        sa.Column("description", sa.String, nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), nullable=False, server_default=sa.func.now()
        ),
        sa.Column(
            "updated_at", sa.DateTime(), nullable=False, server_default=sa.func.now()
        ),
    )

    op.execute(
        """
    CREATE TRIGGER skills_updated_at_trigger
    BEFORE UPDATE ON skills
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
    """
    )

    op.create_table(
        "worker_skills",
        sa.Column(
            "worker_id",
            UUID,
            ForeignKey("workers.id", ondelete="CASCADE", onupdate="CASCADE"),
            nullable=False,
            primary_key=True,
        ),
        sa.Column(
            "skill_id",
            UUID,
            ForeignKey("skills.id", ondelete="CASCADE", onupdate="CASCADE"),
            nullable=False,
            primary_key=True,
        ),
        sa.Column(
            "created_at", sa.DateTime(), nullable=False, server_default=sa.func.now()
        ),
    )


def downgrade():
    op.drop_table("worker_skills")
    op.execute("DROP TRIGGER IF EXISTS skills_updated_at_trigger ON skills;")
    op.drop_table("skills")
    op.execute("DROP TRIGGER IF EXISTS workers_updated_at_trigger ON workers;")
    op.drop_table("workers")
    op.execute("DROP TRIGGER IF EXISTS positions_updated_at_trigger ON positions;")
    op.drop_table("positions")
