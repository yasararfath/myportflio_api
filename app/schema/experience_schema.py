from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class ExperienceCreate(BaseModel):
    designation: str
    company_name: str
    start_year: int
    end_year: int
    location: str
    description: Optional[str] = None

    class Config:
        orm_mode = True


class ExperienceResponse(ExperienceCreate):
    id: int
    user_id: int
    created_at: datetime
