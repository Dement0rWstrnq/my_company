from uuid import UUID

from .worker import Worker
from .base import BaseModel


class Department(BaseModel):
    id: UUID
    name: str
    # worker: Worker
