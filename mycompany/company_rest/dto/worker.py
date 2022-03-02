from uuid import UUID

# from .position import Position
# from .department import Department
# from .skill import Skill
from .base import BaseModel


class Worker(BaseModel):
    id: UUID
    surname: str
    name: str
    # position: Position
    # department: Department
    # skill: Skill
