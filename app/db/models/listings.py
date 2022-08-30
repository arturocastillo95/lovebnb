from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid

from db.base_class import Base

def create_uuid():
    return str(uuid.uuid4())

class Listing(Base):
    """
    Listing Model
    """
    __tablename__ = 'listings'
    id = Column(String(36), primary_key=True, default=create_uuid)
    title = Column(String(64), nullable=False)
    description = Column(String(256), nullable=False)
    price = Column(Float, nullable=False)
    bedrooms = Column(Integer, nullable=False)
    bathrooms = Column(Integer, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, onupdate=func.now())
    host_id = Column(String(36), ForeignKey('users.id'), nullable=False)
    host = relationship('User', back_populates='listings')

    location = relationship('ListingLocation', uselist=False, back_populates='listing')

    def __repr__(self):
        return f'<Listing(id={self.id}, title={self.title})>'

    def to_dict(self):
        data = {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'bedrooms': self.bedrooms,
            'bathrooms': self.bathrooms,
            'is_active': self.is_active,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'host_id': self.host_id,
        }
        return data

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

class ListingLocation(Base):
    """
    Listing Location Model
    """
    __tablename__ = 'listing_locations'
    id = Column(String(36), primary_key=True, default=create_uuid)
    listing_id = Column(String(36), ForeignKey('listings.id'))
    listing = relationship('Listing', back_populates='location')
    address = Column(String(128), nullable=False)
    zipcode = Column(String(5), nullable=False)
    city = Column(String(64), nullable=False)
    state = Column(String(2), nullable=False)
    country = Column(String(64), nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=True)

    def __repr__(self):
        return f'<ListingLocation(id={self.id}, listing_id={self.listing_id})>'

    def to_dict(self):
        return {
            'id': self.id,
            'listing_id': self.listing_id,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

    def from_dict(self, data):
        for field in ['latitude', 'longitude']:
            if field in data:
                setattr(self, field, data[field])
        if 'created_at' in data:
            setattr(self, 'created_at', data['created_at'])
        if 'updated_at' in data:
            setattr(self, 'updated_at', data['updated_at'])

    def __eq__(self, other):
        return self.id == other.id

    def __ne__(self, other):
        return not self.__eq__(other)