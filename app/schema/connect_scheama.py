from datetime import datetime
from pydantic import BaseModel


class ConnectCreate(BaseModel):
    connect_name: str
    image_url: str
    url: str

    class Config:
        orm_mode = True


class ConnectResponse(ConnectCreate):
    id: int
    user_id: int
    created_at: datetime
