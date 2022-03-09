from uuid import UUID
from datetime import datetime

from .base import BaseModel


class Position(BaseModel):
    id: UUID
    name: str
    created_at: datetime
    updated_at: datetime

    class New(BaseModel):
        name: str

    class Update(BaseModel):
        name: str
