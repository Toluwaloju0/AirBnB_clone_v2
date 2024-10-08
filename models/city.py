#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    # columns
    state_id = Column(String(60), ForeignKey('states.id'))
    name = Column(String(128), nullable=False)

    # relationship
    state = relationship('State', back_populates='cities')
    places = relationship(
        'Place',
        back_populates='cities',
        cascade='all, delete, delete-orphan')
