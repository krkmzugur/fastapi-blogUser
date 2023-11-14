from fastapi import APIRouter,Depends,status,HTTPException
from .. import schemas,database,models,oauth2
from typing import List
from sqlalchemy.orm import Session
from ..repository import user

get_db = database.get_db

router =APIRouter(
    prefix="/user",
    tags=['Users']
)


@router.post('/',response_model=schemas.ShowUser)
def create(request : schemas.User,db: Session = Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
  return user.create(db,request)


@router.put('/{id}',response_model=schemas.ShowUser)
def get_user(id:int,db:Session =Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
   return user.get_user(db,id)