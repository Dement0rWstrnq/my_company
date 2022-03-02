from .base import BaseModel

from uuid import UUID


class WorkerSkill(BaseModel):
    worker_id: UUID
    skill_id: UUID
