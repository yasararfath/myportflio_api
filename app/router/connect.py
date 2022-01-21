from fastapi import APIRouter, status, Depends
from app.database import get_db
from app.oauth2 import get_current_user
from app.models import Connect
from app.crud.item import item_obj
from sqlalchemy.orm.session import Session
from app.schema.connect_scheama import ConnectCreate, ConnectResponse
from typing import List

router = APIRouter(prefix="/connect", tags=["Connect"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ConnectResponse)
def create_connect(
    connect: ConnectCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    connect_data = Connect(user_id=current_user, **connect.dict())
    res = item_obj.create(db=db, row=connect_data)
    return res


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[ConnectResponse])
def get_connect_all(
    db: Session = Depends(get_db), current_user: int = Depends(get_current_user)
):
    res = item_obj.get_all(db=db, table=Connect)
    return res


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=ConnectResponse)
def get_connect(
    id: int,
    db: Session = Depends(get_db),
    current_user: int = Depends(get_current_user),
):
    res = item_obj.get_all(db=db, table=Connect, id=id)
    return res


@router.put("/{about_id}", response_model=ConnectResponse)
def edit_connect(
    connect_id: int,
    updated_content: ConnectCreate,
    db: Session = Depends(get_db),
    current_user: int = Depends(get_current_user),
):
    res = item_obj.put(
        db=db, table=Connect, id=connect_id, row=updated_content, user_id=current_user
    )
    return res


@router.delete("/{about_id}")
def delete_connect(
    connect_id: int,
    db: Session = Depends(get_db),
    current_user: int = Depends(get_current_user),
):
    res = item_obj.delete(db=db, table=Connect, id=connect_id, user_id=current_user)
    return res
