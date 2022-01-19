from fastapi import APIRouter, status, Depends, HTTPException
from app.database import get_db
from sqlalchemy.orm.session import Session
from app.models import User
from app.utils import verify
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from app.oauth2 import create_access_token

router = APIRouter(prefix="/login", tags=["User"])


@router.post("/", status_code=status.HTTP_200_OK)
def user_login(
    user: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    response = db.query(User).filter(User.email == user.username).first()
    if not response:
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail="Invalid Credientials")
    if not verify(user.password, response.password):
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail="Invalid credentials")
    access_token = create_access_token({"id": response.id})
    return {"token_type": "Bearer", "token": access_token}
