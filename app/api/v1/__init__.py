from fastapi import APIRouter
from api.v1 import route_users, route_listings

api_router = APIRouter()

api_router.include_router(route_users.router, prefix="/users", tags=["users"])
api_router.include_router(route_listings.router, prefix="/listings", tags=["listings"])