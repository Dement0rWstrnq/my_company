import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from ..base import Base


class Department(Base):
    __tablename__ = "departments"

    id = sa.Column(
        UUID(as_uuid=True), primary_key=True, server_default=sa.func.uuid_generate_v1()
    )
    name = sa.Column(sa.String, nullable=False)
    created_at = sa.Column(sa.DateTime(), nullable=False, server_default=sa.func.now())
    updated_at = sa.Column(sa.DateTime(), nullable=False, server_default=sa.func.now())

    workers = relationship("Worker", cascade="all,delete", back_populates="department")

    def __repr__(self):
        return f"<Department id={self.id}>"
