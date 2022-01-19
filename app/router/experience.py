from fastapi import APIRouter, status, Depends
from app.database import get_db
from app.oauth2 import get_current_user
from app.models import Experience
from app.crud.item import item_obj
from sqlalchemy.orm.session import Session
from app.schema.experience_schema import ExperienceResponse, ExperienceCreate
from typing import List

router = APIRouter(prefix="/experience", tags=["Experience"])


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=ExperienceResponse
)
def create_experience(
    experience: ExperienceCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    experience_data = Experience(user_id=current_user, **experience.dict())
    res = item_obj.create(db=db, row=experience_data)
    return res


@router.get(
    "/", status_code=status.HTTP_200_OK, response_model=List[ExperienceResponse]
)
def get_experience_all(
    db: Session = Depends(get_db), current_user: int = Depends(get_current_user)
):
    res = item_obj.get_all(db=db, table=Experience)
    return res


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=ExperienceResponse)
def get_experience(
    id: int,
    db: Session = Depends(get_db),
    current_user: int = Depends(get_current_user),
):
    res = item_obj.get_all(db=db, table=Experience, id=id)
    return res


@router.put("/{about_id}")
def edit_experience(
    about_id: int,
    updated_content: ExperienceCreate,
    db: Session = Depends(get_db),
    current_user: int = Depends(get_current_user),
):

    res = item_obj.put(
        db=db, table=Experience, id=about_id, row=updated_content, user_id=current_user
    )

    return res


@router.delete("/{about_id}")
def delete_experience(
    about_id: int,
    db: Session = Depends(get_db),
    current_user: int = Depends(get_current_user),
):
    res = item_obj.delete(db=db, table=Experience, id=about_id, user_id=current_user)
    return res
