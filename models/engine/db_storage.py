#!/usr/bin/python3
"""A module to use ORMs"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


class DBStorage:
    """A class to create a new engine"""

    __engine = None
    __session = None

    def __init__(self):
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')

        DBStorage.__engine = create_engine('mysql+mysqldb://{}:{}@{}/\
{}'.format(user, pwd, host, db), pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metedata.dropall()

    def all(self, cls=None):
        """A mehod to create a query a database"""
        Dictionary = {}
        if cls is None:
            result = DBStorage.__session.\
                query(User, State, City, Amenity, Place, Review).all()
        else:
            result = DBStoragew.query(cls).all
        for a in result:
            Dictionary['{}.{}'.format(a.__class__.__name, a.id)] = a
        return dictionary

    def new(self, obj):
        """To add obt to the database session"""
        self.__storage.add(obj)

    def save(self):
        """To commit session to the database"""
        self.__storage.commit()

    def delete(self, obj=None):
        """Tom delete an obj from a database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """To create tables in  a database"""
        from models.city import City
        from models.state import State

        Base.metadata.create_all()
        Session_1 = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(Session_1)
        self.__session = Session()
