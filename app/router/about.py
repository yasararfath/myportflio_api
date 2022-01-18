from fastapi import APIRouter, status, Depends
from app.models import About
from app.schema.about_schema import CreateAbout, CreateAboutResponse
from sqlalchemy.orm.session import Session
from app.models import About
from app.database import get_db
from typing import Any, List
from app.oauth2 import get_current_user
from app.crud.item import item_obj

router = APIRouter(prefix="/about", tags=["About"])


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=CreateAboutResponse
)
def create_about(
    about: CreateAbout,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    about_data = About(user_id=current_user.id, **about.dict())
    res = item_obj.create(db=db, row=about_data)
    return res


@router.get(
    "/", status_code=status.HTTP_200_OK, response_model=List[CreateAboutResponse]
)
def get_about_all(
    db: Session = Depends(get_db), current_user: int = Depends(get_current_user)
) -> Any:
    res = item_obj.get_all(db=db, table=About)
    return res


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=CreateAboutResponse)
def get_about(
    id: int,
    db: Session = Depends(get_db),
    current_user: int = Depends(get_current_user),
) -> Any:
    res = item_obj.get_all(db=db, table=About, id=id)
    return res


@router.put("/{about_id}")
def edit_about(
    about_id: int,
    updated_content: CreateAbout,
    db: Session = Depends(get_db),
    current_user: int = Depends(get_current_user),
) -> Any:
    res = item_obj.put(
        db=db, table=About, id=about_id, row=updated_content, user_id=current_user
    )
    return res


@router.delete("/{about_id}")
def delete_about(
    about_id: int,
    db: Session = Depends(get_db),
    current_user: int = Depends(get_current_user),
) -> Any:
    res = item_obj.delete(db=db, table=About, id=about_id, user_id=current_user)
    return res
