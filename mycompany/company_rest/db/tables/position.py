import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

from ..base import Base


class Position(Base):
    __tablename__ = "positions"

    id = sa.Column(
        UUID(as_uuid=True), primary_key=True, server_default=sa.func.uuid_generate_v1()
    )
    name = sa.Column(sa.String, nullable=False)
    created_at = sa.Column(sa.DateTime(), nullable=False, server_default=sa.func.now())
    updated_at = sa.Column(sa.DateTime(), nullable=False, server_default=sa.func.now())

    def __repr__(self):
        return f"<Position id={self.id}>"
