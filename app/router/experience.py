from fastapi import APIRouter,status, Depends
from app.database import get_db
from app.oauth2 import get_current_user
from app.models import Experience
from app.crud.crud import crud_obj
from sqlalchemy.orm.session import Session
from app.schema.experience_schema import ExperienceResponse,ExperienceCreate
from typing import List
router = APIRouter(
    prefix="/experience",
    tags=['Experience']
)

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=ExperienceResponse)
def create_education(education:ExperienceCreate,db:Session=Depends(get_db),current_user:str=Depends(get_current_user)):
    education_data = Experience(user_id=current_user.id,**education.dict())
    res = crud_obj.create(db=db,row=education_data)
    # db.add(about_data)
    # db.commit()
    # db.refresh(about_data)

    return res

@router.get("/",status_code=status.HTTP_200_OK,response_model=List[ExperienceResponse])
def get_about(db:Session=Depends(get_db),current_user:int=Depends(get_current_user)):
    res = crud_obj.get_all(db=db,table=Experience)
    # res = db.query(About).all()
    # if res is None:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No Data Found")  
    return res

@router.get("/{id}",status_code=status.HTTP_200_OK,response_model=ExperienceResponse)
def get_about(id:int,db:Session=Depends(get_db),current_user:int=Depends(get_current_user)):
    res = crud_obj.get_all(db=db,table=Experience,id=id)
    # res = db.query(About).all()
    # if res is None:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No Data Found")  
    return res

@router.put("/{about_id}")
def edit_about(about_id:int,updated_post:ExperienceCreate,db:Session=Depends(get_db),current_user:int=Depends(get_current_user)):

    res = crud_obj.put(db=db,table=Experience,id=about_id,row=updated_post)
    
    return res

@router.delete("/{about_id}")
def delete_about(about_id:int,db:Session=Depends(get_db),current_user:int=Depends(get_current_user)):
    res = crud_obj.delete(db=db,table=Experience,id=about_id)
    # res = db.query(About).get(about_id)

    # if res is None:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No Data Found")
    
    # db.delete(res)
    # db.commit()
    
    return res
