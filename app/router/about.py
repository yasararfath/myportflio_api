from fastapi import APIRouter,status,Depends,HTTPException
from app.models import About
from app.schema.about_schema import CreateAbout,CreateAboutResponse
from sqlalchemy.orm.session import Session
from app.models import About
from app.database import get_db
from typing import List
from app.oauth2 import get_current_user
from app.crud.crud import crud_obj

router = APIRouter(prefix='/about',
                tags=['About'])

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=CreateAboutResponse)
def create_about(about:CreateAbout,db:Session=Depends(get_db),current_user:str=Depends(get_current_user)):
    about_data = About(user_id=current_user.id,**about.dict())
    res = crud_obj.create(db=db,row=about_data)
    # db.add(about_data)
    # db.commit()
    # db.refresh(about_data)

    return res

@router.get("/",status_code=status.HTTP_200_OK,response_model=List[CreateAboutResponse])
def get_about(db:Session=Depends(get_db),current_user:int=Depends(get_current_user)):
    res = crud_obj.get_all(db=db,table=About)
    # res = db.query(About).all()
    # if res is None:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No Data Found")
    
    return res

@router.put("/{about_id}")
def edit_about(about_id:int,updated_post,db:Session=Depends(get_db),current_user:int=Depends(get_current_user)):
    res = crud_obj.put(db=db,table=About,id=about_id,row=updated_post)
    
    return res

@router.delete("/{about_id}")
def delete_about(about_id:int,db:Session=Depends(get_db),current_user:int=Depends(get_current_user)):
    res = crud_obj.delete(db=db,table=About,id=about_id)
    # res = db.query(About).get(about_id)

    # if res is None:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No Data Found")
    
    # db.delete(res)
    # db.commit()
    
    return res
