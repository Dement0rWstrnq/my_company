from uuid import UUID
from datetime import datetime

from .position import Position
from .department import Department
from .skill import Skill
from .base import BaseModel


class Worker(BaseModel):
    id: UUID
    name: str
    surname: str
    department: Department
    position: Position
    created_at: datetime
    updated_at: datetime
    skills: list[Skill] = []

    class New(BaseModel):
        name: str
        surname: str
        department_id: UUID
        position_id: UUID
        skills: list[UUID] | list = []

    class Update(BaseModel):
        name: str
        surname: str
        department_id: UUID
        position_id: UUID
        skills: list[UUID] | list = []
