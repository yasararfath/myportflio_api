from fastapi import APIRouter, status, Depends
from app.database import get_db
from app.oauth2 import get_current_user
from app.models import Certification
from app.crud.item import item_obj
from sqlalchemy.orm.session import Session
from app.schema.certification_schema import CertificationCreate, CertificationResponse
from typing import List

router = APIRouter(prefix="/certificate", tags=["Certification"])


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=CertificationResponse
)
def create_certification(
    certification: CertificationCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    certification_data = Certification(user_id=current_user, **certification.dict())
    res = item_obj.create(db=db, row=certification_data)
    return res


@router.get(
    "/", status_code=status.HTTP_200_OK, response_model=List[CertificationResponse]
)
def get_certification_all(
    db: Session = Depends(get_db), current_user: int = Depends(get_current_user)
):
    res = item_obj.get_all(db=db, table=Certification)
    return res


@router.get(
    "/{id}", status_code=status.HTTP_200_OK, response_model=CertificationResponse
)
def get_certification(
    id: int,
    db: Session = Depends(get_db),
    current_user: int = Depends(get_current_user),
):
    res = item_obj.get_all(db=db, table=Certification, id=id)
    return res


@router.put("/{about_id}", response_model=CertificationResponse)
def edit_certification(
    certification_id: int,
    updated_content: CertificationCreate,
    db: Session = Depends(get_db),
    current_user: int = Depends(get_current_user),
):
    res = item_obj.put(
        db=db,
        table=Certification,
        id=certification_id,
        row=updated_content,
        user_id=current_user,
    )
    return res


@router.delete("/{about_id}")
def delete_certification(
    certification_id: int,
    db: Session = Depends(get_db),
    current_user: int = Depends(get_current_user),
):
    res = item_obj.delete(
        db=db, table=Certification, id=certification_id, user_id=current_user
    )
    return res
