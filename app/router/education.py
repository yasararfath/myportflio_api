from dataclasses import dataclass
from re import I
from fastapi import APIRouter, status, Depends
from app.database import get_db
from app.oauth2 import get_current_user
from app.models import Education
from app.crud.item import item_obj
from sqlalchemy.orm.session import Session
from app.schema.education_schema import EducationCreate, EducationResponse
from typing import List

router = APIRouter(prefix="/education", tags=["Eduaction"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=EducationResponse)
def create_education(
    education: EducationCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    education_data = Education(user_id=current_user, **education.dict())
    res = item_obj.create(db=db, row=education_data)
    return res


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[EducationResponse])
def get_education_all(
    db: Session = Depends(get_db), current_user: int = Depends(get_current_user)
):
    res = item_obj.get_all(db=db, table=Education)
    return res


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=EducationResponse)
def get_education(
    id: int,
    db: Session = Depends(get_db),
    current_user: int = Depends(get_current_user),
):
    res = item_obj.get_all(db=db, table=Education, id=id)
    return res


@router.put("/{about_id}")
def edit_education(
    about_id: int,
    updated_content: EducationCreate,
    db: Session = Depends(get_db),
    current_user: int = Depends(get_current_user),
):

    res = item_obj.put(
        db=db, table=Education, id=about_id, row=updated_content, user_id=current_user
    )

    return res


@router.delete("/{about_id}")
def delete_education(
    about_id: int,
    db: Session = Depends(get_db),
    current_user: int = Depends(get_current_user),
):
    res = item_obj.delete(db=db, table=Education, id=about_id, user_id=current_user)
    return res
