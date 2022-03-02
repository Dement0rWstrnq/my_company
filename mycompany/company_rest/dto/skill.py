from uuid import UUID
from .base import BaseModel


class Skill(BaseModel):
    id: UUID
    name: str
    description: str
