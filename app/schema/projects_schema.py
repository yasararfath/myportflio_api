from datetime import datetime
from pydantic import BaseModel


class ProjectCreate(BaseModel):
    project_name: str
    project_description: str
    url: str

    class Config:
        orm_mode = True


class ProjectResponse(ProjectCreate):
    id: int
    user_id: int
    created_at: datetime
