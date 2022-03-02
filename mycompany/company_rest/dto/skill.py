from uuid import UUID
from datetime import datetime

from .base import BaseModel


class Skill(BaseModel):
    id: UUID
    name: str
    description: str
    created_at: datetime
    updated_at: datetime
