from email.policy import default
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from typing import Optional
import uuid
# from sqlmodel import SQLModel, Field

from db.base_class import Base

def create_uuid():
    return str(uuid.uuid4())

class User(Base):
    __tablename__   = 'users'
    id              = Column(String(36), primary_key=True, default=create_uuid)
    first_name      = Column(String(50), nullable=False)
    last_name       = Column(String(50), nullable=False)
    email           = Column(String(64), nullable=False, unique=True)
    is_active       = Column(Boolean, default=True, nullable=False)
    is_admin        = Column(Boolean, default=False, nullable=False)
    password        = Column(String(128), nullable=False)
    created_at      = Column(DateTime, default=func.now())
    updated_at      = Column(DateTime, default=func.now(), onupdate=func.now())
    listings        = relationship("Listing", back_populates="host")

    def __repr__(self):
        return f'<User(id={self.id}, email={self.email})>'
    
    def response_dict(self):
        return {
            'email': self.email,
            'is_active': self.is_active,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }

# class User(SQLModel, table=True):
#     id: Optional[str] = Field(String(36), primary_key=True, default=create_uuid)