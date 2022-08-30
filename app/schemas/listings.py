from turtle import title
from pydantic import BaseModel

class CreateListing(BaseModel):
    title: str
    description: str
    price: float
    bedrooms: int
    bathrooms: int
    host_id: str
    address: str
    zipcode: str
    city: str
    state: str
    country: str
    latitude: float
    longitude: float