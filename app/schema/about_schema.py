from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CreateAbout(BaseModel):
    name: str
    designation: str
    email: str
    phone:str
    location:str
    objective: Optional[str] = ""
    user_id : int

    class Config:
        orm_mode = True

class CreateAboutResponse(CreateAbout):
    created_at: datetime