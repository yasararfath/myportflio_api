from fastapi import APIRouter, Depends,status
from app.models import User
from sqlalchemy.orm.session import Session
from app.database import get_db
from app.schema.user_schema import UserResponse,Users
from app.utils import hash_password

router = APIRouter(prefix="/user",tags=['User'])


@router.post("/",status_code=status.HTTP_201_CREATED,response_model=UserResponse)
def create_user(userCreate:Users,db:Session=Depends(get_db)):
    userCreate.password = hash_password(userCreate.password)
    user = User(**userCreate.dict())
    db.add(user)
    db.commit()
    db.refresh(user)

    return user
