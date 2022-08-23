from fastapi import FastAPI, Depends
from core.config import settings
from db.session import engine
from db.base import Base
# import uvicorn

# from sqlalchemy.orm import Session
# from schemas.users import CreateUser
# from crud.users import create_new_user

from api.v1 import api_router


def create_tables(engine):
    Base.metadata.create_all(bind=engine)

def start_app():
    app = FastAPI(title=settings.PROJECT_TITLE, description=settings.PROJECT_DESCRIPTION, version=settings.PROJECT_VERSION)
    create_tables(engine)
    app.include_router(api_router)
    return app

app = start_app()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# @app.get("/create-listing")
# async def create_listing():
#     return {"message": "Create Listing"}

# @app.get("/listings")
# async def listings():
#     return {"message": "Listings"}

# @app.post("/create-user")
# async def create_user(user: CreateUser, db: Session = Depends(get_db)):
#     return create_new_user(db=db, user=user)

 