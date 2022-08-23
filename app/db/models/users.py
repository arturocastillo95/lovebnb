from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, Float
from sqlalchemy.orm import relationship

from db.base_class import Base

class User(Base):
    __tablename__   = 'users'
    id              = Column(Integer, primary_key=True)
    name            = Column(String(64), nullable=False)
    email           = Column(String(64), nullable=False)
    is_active       = Column(Boolean, default=True, nullable=False)
    is_admin        = Column(Boolean, default=False, nullable=False)
    password        = Column(String(128), nullable=False)
    created_at      = Column(DateTime, default=None, nullable=True)
    updated_at      = Column(DateTime, default=None, nullable=True)
    listings        = relationship("Listing", back_populates="host")