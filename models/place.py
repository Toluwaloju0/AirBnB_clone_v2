#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship


place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column(
        'places_id',
        String(60),
        ForeignKey('places.id'),
        primary_key=True),
    Column(
        'amenities_id',
        String(60),
        ForeignKey('amenities.id'),
        primary_key=True)
)


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    # column
    city_id = Column(String(60), ForeignKey('cities.id'))
    user_id = Column(String(60), ForeignKey('users.id'))
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)

    # relationship
    user = relationship('User', back_populates='places')
    cities = relationship('City', back_populates='places')
    reviews = relationship(
        'Review',
        back_populates='place',
        cascade='all, delete, delete-orphan')
    amenities = relationship(
        'Amenity',
        secondary=place_amenity,
        viewonly=False)
    amenity_ids = []
