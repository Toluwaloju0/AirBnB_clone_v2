#!/usr/bin/python3
""" A module to strore information througha a database"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from os import getenv


class DBStorage():
    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        pword = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        dbase = getenv("HBNB_MYSQL_DB")
        DBStorage.__engine = create_engine(
            f"mysql+mysqldb://{user}:{pword}@{host}/{dbase}",
            pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(DBStorage.__engine)

    def all(self, cls=None):
        """A method to query a dunction"""

        from models.base_model import BaseModel, Base
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User

        DBdict = {}
        Classes = [User, State, City, Amenity, Place, Review]
        DBStorage.__session = Session(bind=engine)
        if cls:
            DBclass = DBStorage.__session.query(cls).all()
            for obj in DBclass:
                key = obj.__class__.__name__ + '.' + obj.id
                DBdict[key] = obj
        else:
            for cls in Classes:
                DBclass = DBStorage.__session.query(cls).all()
                for obj in DBclass:
                    key = obj.__class__.__name___ + '.' + obj.id
                    DBdict[key] = obj
        return DBdict

    def new(self, obj):
        """To add the obj to the current session"""
        DBStorage.__session.add(obj)

    def save(self):
        """To commit all the changes to the database"""
        DBStorage.__session.commit()

    def delete(self, obj=None):
        """T delete from  the database"""
        if obj:
            DBstorage.__session.delete(obj)

    def reload(self):
        """To create all the tables to the database"""

        from models.base_model import BaseModel, Base
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User
        from sqlalchemy.orm import sessionmaker, scoped_session

        # create all classes in the database
        Base.metadata.create_all(DBStorage.__engine)
        # create a session
        Session = scoped_session(
            sessionmaker(bind=DBStorage.__engine, expire_on_commit=False))
        DBStorage.__session = Session()
