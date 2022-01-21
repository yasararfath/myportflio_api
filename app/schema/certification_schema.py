from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class CertificationCreate(BaseModel):
    certification_name: str
    issue_from: str
    issue_by: str
    expire_year: Optional[str] = ""
    description: Optional[str] = ""
    url = str

    class Config:
        orm_mode = True


class CertificationResponse(CertificationCreate):
    id: int
    user_id: int
    created_at: datetime
