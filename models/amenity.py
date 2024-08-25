#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from models.Place import place_amenity


class Amenity(BaseModel, Base):
    """A class for the table amenities"""
    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)
    place_amenity = relationship(
        'Place',
        secondary=place_amenity,
        view_only=False
    )
