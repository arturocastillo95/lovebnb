from sqlalchemy.orm import Session

from schemas.users import CreateUser
from db.models.users import User

def create_new_user(db: Session, user: CreateUser) -> User:
    db_user = User(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        password=user.password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user