from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, Float
from sqlalchemy.orm import relationship
import uuid

from db.base_class import Base

def create_uuid():
    return str(uuid.uuid4())

class User(Base):
    __tablename__   = 'users'
    id              = Column(String(36), primary_key=True, default=create_uuid)
    first_name      = Column(String(50), nullable=False)
    last_name       = Column(String(50), nullable=False)
    email           = Column(String(64), nullable=False)
    is_active       = Column(Boolean, default=True, nullable=False)
    is_admin        = Column(Boolean, default=False, nullable=False)
    password        = Column(String(128), nullable=False)
    created_at      = Column(DateTime, default=None, nullable=True)
    updated_at      = Column(DateTime, default=None, nullable=True)
    listings        = relationship("Listing", back_populates="host")