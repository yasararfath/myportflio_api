from pydantic import BaseModel,EmailStr
from datetime import datetime

class CreateUserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    class Config:
        orm_mode = True
    
class CreateUser(BaseModel):
    password: str
    email: EmailStr

    class Config:
        orm_mode = True

class TokenData(BaseModel):
    email:str

    class Config:
        orm_mode = True