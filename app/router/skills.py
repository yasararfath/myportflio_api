from fastapi import APIRouter, status, Depends
from app.database import get_db
from app.oauth2 import get_current_user
from app.models import Skills
from app.crud.item import item_obj
from sqlalchemy.orm.session import Session
from app.schema.skill_schema import SkillCreate, SkillResponse
from typing import List

router = APIRouter(prefix="/skills", tags=["Skills"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=SkillResponse)
def create_skill(
    skill: SkillCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    skill_data = Skills(user_id=current_user, **skill.dict())
    res = item_obj.create(db=db, row=skill_data)
    return res


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[SkillResponse])
def get_skill_all(
    db: Session = Depends(get_db), current_user: int = Depends(get_current_user)
):
    res = item_obj.get_all(db=db, table=Skills)
    return res


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=SkillResponse)
def get_skill(
    id: int,
    db: Session = Depends(get_db),
    current_user: int = Depends(get_current_user),
):
    res = item_obj.get_all(db=db, table=Skills, id=id)
    return res


@router.put("/{about_id}", status_code=status.HTTP_200_OK, response_model=SkillResponse)
def edit_skill(
    skill_id: int,
    updated_content: SkillCreate,
    db: Session = Depends(get_db),
    current_user: int = Depends(get_current_user),
):
    res = item_obj.put(
        db=db, table=Skills, id=skill_id, row=updated_content, user_id=current_user
    )
    return res


@router.delete("/{about_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_skill(
    skill_id: int,
    db: Session = Depends(get_db),
    current_user: int = Depends(get_current_user),
):
    res = item_obj.delete(db=db, table=Skills, id=skill_id, user_id=current_user)
    return res
