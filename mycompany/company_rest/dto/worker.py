from uuid import UUID
from datetime import datetime

from .department import Department
from .skill import Skill
from .base import BaseModel


class Worker(BaseModel):
    id: UUID
    surname: str
    name: str
    created_at: datetime
    updated_at: datetime
    skill: list[Skill]
    department: Department