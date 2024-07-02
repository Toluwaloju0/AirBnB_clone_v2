#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Metadata
from sqlalchemy.orm import Relationship


metadata = MetaData()
place_amenities = Table('place_amenity', metadata, Column('place_id', String(60), nullable=False, ForeignKey('place.id'), primary_key=True), Column('amenity_id', string(60), nullable=False, ptimary_key=True, ForeignKey('amenities.id'))

class Amenity(BaseModel, Base):
    """The amenity class"""
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = Relationship('Place', secondary=place_amenities, back_populates='amenities')
