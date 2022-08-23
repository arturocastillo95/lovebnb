from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.users import CreateUser
from db.session import get_db
from crud.users import create_new_user

router = APIRouter()

@router.post("/create-user")
def create_user(user: CreateUser, db: Session = Depends(get_db)):
    return create_new_user(db=db, user=user)