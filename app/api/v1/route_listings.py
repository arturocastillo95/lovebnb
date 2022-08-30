from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.listings import CreateListing
from db.session import get_db
from crud.listings import create_new_listing

router = APIRouter()

@router.post("/create-listing")
def create_listing(listing: CreateListing, db: Session = Depends(get_db)):
    return create_new_listing(db=db, listing=listing)