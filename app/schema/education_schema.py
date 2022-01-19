from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class EducationCreate(BaseModel):
    school_name: str
    grade: int
    out_of: int
    degree: str
    start_year: int
    end_year: int
    location: str
    description: Optional[str] = None

    class Config:
        orm_mode = True


class EducationResponse(EducationCreate):
    id: int
    user_id: int
    created_at: datetime
