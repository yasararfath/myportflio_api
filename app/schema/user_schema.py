from pydantic import BaseModel,EmailStr


class UserResponse(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True
    
class Users(BaseModel):
    password: str
    email: EmailStr

    class Config:
        orm_mode = True

class TokenData(BaseModel):
    email:str

    class Config:
        orm_mode = True