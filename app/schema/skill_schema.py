from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class SkillCreate(BaseModel):
    skill_type: str
    skill_name: str

    class Config:
        orm_mode = True


class SkillResponse(SkillCreate):
    id: int
    user_id: int
    created_at: datetime
