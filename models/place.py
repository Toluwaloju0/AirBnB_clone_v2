#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, String, Integer, Float, MetaData
from sqlalchemy.orm import Relationship


metadata = MetaData()


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), nullable=False, ForeignKey('cities.id'))
    user_id = Column(String(60), nullable=False, ForeignKey('user.id'))
    name = Column(String(128), nullable-False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, defaule=0)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    reviews = Relationship('Review', backref='place')
    amenities = Relationship('Amenity', secondary=place_amenity, view_only=False)


place_amenity = Table('place_amenity', metadata, Column('place_id', String(60), nullable=False, ForeignKey('place.id'), primary_key=True), Column('amenity_id', string(60), nullable=False, ptimary_key=True, ForeignKey('amenities.id'))
