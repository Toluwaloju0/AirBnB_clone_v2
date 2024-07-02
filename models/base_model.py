#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime


Base = declarative_base()

class BaseModel:
    """A base class for all hbnb models"""
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = Column(String(60), nullable=False, primary_key=True)
            self.created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
            self.updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())
        else:
            kwargs['updated_at'] = Column(DateTime, nullable=False, default=datetime.utcnow())
            kwargs['created_at'] = Column(DateTime, nullable=False, default=datetime.utcnow())
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        for key in dictionary.keys():
            if key == '_sa_instance_state':
                del dictionary[key]
                return
        return dictionary
    def delete(self):
        """To delete an instance using storage.delete"""
        storage.delete(self)
