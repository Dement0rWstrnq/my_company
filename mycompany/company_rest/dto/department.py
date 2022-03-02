from uuid import UUID
from datetime import datetime

from .base import BaseModel


class Department(BaseModel):
    id: UUID
    name: str
    created_at: datetime
    updated_at: datetime

