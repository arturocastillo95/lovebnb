from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, Float
from sqlalchemy.orm import relationship

from db.base_class import Base

class Listing(Base):
    """
    Listing Model
    """
    __tablename__ = 'listings'
    id = Column(Integer, primary_key=True)
    host_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    host = relationship('User', back_populates='listings')
    title = Column(String(64), nullable=False)
    description = Column(String(256), nullable=False)
    price = Column(Float, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime, default=None, nullable=True)
    updated_at = Column(DateTime, default=None, nullable=True)

    def __repr__(self):
        return f'<Listing(id={self.id}, title={self.title})>'

    def to_dict(self):
        return {
            'id': self.id,
            'host_id': self.host_id,
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'is_active': self.is_active,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

    def from_dict(self, data):
        for field in ['title', 'description', 'price']:
            if field in data:
                setattr(self, field, data[field])
        if 'is_active' in data:
            setattr(self, 'is_active', data['is_active'])
        if 'created_at' in data:
            setattr(self, 'created_at', data['created_at'])
        if 'updated_at' in data:
            setattr(self, 'updated_at', data['updated_at'])

    def __eq__(self, other):
        return self.id == other.id

    def __ne__(self, other):
        return not self.__eq__(other)