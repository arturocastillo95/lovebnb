from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException

from schemas.listings import CreateListing
from db.models.listings import Listing, ListingLocation
from db.models.users import User

def create_new_listing(db: Session, listing: CreateListing) -> Listing:
    #Check if the host is already in the database if not raise an error
    db_user = db.query(User).filter(User.id == listing.host_id).first()
    
    if not db_user:
        raise HTTPException(status_code=400, detail="The host does not exist")

    db_listing = Listing(
        title=listing.title,
        description=listing.description,
        price=listing.price,
        bedrooms=listing.bedrooms,
        bathrooms=listing.bathrooms,
        host_id=listing.host_id,
    )
    #Add location
    db_location = ListingLocation(
        address=listing.address,
        zipcode=listing.zipcode,
        city=listing.city,
        state=listing.state,
        country=listing.country,
        latitude=listing.latitude,
        longitude=listing.longitude,
    )
    db_listing.location = db_location
    db.add(db_listing)
    db.commit()
    db.refresh(db_listing)
    return db_listing