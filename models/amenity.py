#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.place import place_amenity
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """A class for the table amenities"""
    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)
    place_amenity = relationship(
        'Place',
        secondary=place_amenity,
        viewonly=False,
        back_populates='amenities'
    )
