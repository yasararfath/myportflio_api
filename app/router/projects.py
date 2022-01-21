from fastapi import APIRouter, status, Depends
from app.database import get_db
from app.oauth2 import get_current_user
from app.models import Projects
from app.crud.item import item_obj
from sqlalchemy.orm.session import Session
from app.schema.projects_schema import ProjectCreate, ProjectResponse
from typing import List

router = APIRouter(prefix="/project", tags=["Projects"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ProjectResponse)
def create_project(
    project: ProjectCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    project_data = Projects(user_id=current_user, **project.dict())
    res = item_obj.create(db=db, row=project_data)
    return res


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[ProjectResponse])
def get_project_all(
    db: Session = Depends(get_db), current_user: int = Depends(get_current_user)
):
    res = item_obj.get_all(db=db, table=Projects)
    return res


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=ProjectResponse)
def get_project(
    id: int,
    db: Session = Depends(get_db),
    current_user: int = Depends(get_current_user),
):
    res = item_obj.get_all(db=db, table=Projects, id=id)
    return res


@router.put("/{about_id}", response_model=ProjectResponse)
def edit_project(
    project_id: int,
    updated_content: ProjectCreate,
    db: Session = Depends(get_db),
    current_user: int = Depends(get_current_user),
):
    res = item_obj.put(
        db=db, table=Projects, id=project_id, row=updated_content, user_id=current_user
    )
    return res


@router.delete("/{about_id}")
def delete_project(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: int = Depends(get_current_user),
):
    res = item_obj.delete(db=db, table=Projects, id=project_id, user_id=current_user)
    return res
