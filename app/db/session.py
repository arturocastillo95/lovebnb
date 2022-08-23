from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from typing import Generator

SQLALCHEMY_DATABASE_URL = "sqlite:///./db.sqlite"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Generator[SessionLocal, None, None]:
    """
    Returns a database session
    """
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()