import sqlalchemy as sa
from sqlalchemy import ForeignKey, func, event
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship, query_expression
from sqlalchemy.orm import object_session

from ..base import Base


class Worker(Base):
    __tablename__ = "workers"

    id = sa.Column(
        UUID(as_uuid=True), primary_key=True, server_default=sa.func.uuid_generate_v1()
    )
    name = sa.Column(sa.String, nullable=False)
    surname = sa.Column(sa.String, nullable=False)
    department_id = sa.Column(
        UUID(as_uuid=True),
        ForeignKey("departments.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    position_id = sa.Column(
        UUID(as_uuid=True),
        ForeignKey("positions.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    created_at = sa.Column(sa.DateTime(), nullable=False, server_default=sa.func.now())
    updated_at = sa.Column(sa.DateTime(), nullable=False, server_default=sa.func.now())

    department = relationship("Department", back_populates="workers")
    position = relationship("Position", lazy="joined")
    skills = relationship("Skill", secondary="worker_skills")

    # Чтобы был атрибут fullname, который вычисляется на стороне Python
    @hybrid_property
    def fullname(self):
        return f"{self.name} {self.surname}"

    # Чтобы была возможность этот атрибут поменять
    @fullname.setter
    def fullname(self, value):
        self.name, self.surname = value.split(" ")

    # Чтобы была возможность встраивать этот атрибут в SQL запрос
    @fullname.expression
    def fullname(cls):
        return func.concat(cls.name, " ", cls.surname)

    some = query_expression()

    def __repr__(self):
        return f"<Worker id={self.id}>"
