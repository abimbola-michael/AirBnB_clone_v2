#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""
import json
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship, scoped_session
from models.base_model import Base
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """This class manages storage of hbnb models in JSON format"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes db storage class"""
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(
                getenv("HBNB_MYSQL_USER"),
                getenv("HBNB_MYSQL_PWD"),
                getenv("HBNB_MYSQL_HOST"),
                getenv("HBNB_MYSQL_DB")
                ), pool_pre_ping=True
            )
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        newDict = {}

        if cls is None:
            objects = self.__session.query(State).all()
            objects.extend(self.__session.query(City).all())
            objects.extend(self.__session.query(Place).all())
            objects.extend(self.__session.query(Amenity).all())
            objects.extend(self.__session.query(User).all())
            objects.extend(self.__session.query(Review).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            objects = self.__session.query(cls)
        return {
                "{}.{}".format(
                    type(obj).__name__, obj.id
                    ): obj for obj in objects
                }

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__session.add(obj)

    def save(self):
        """Saves objects to database"""
        self.__session.commit()

    def reload(self):
        """Loads storage dictionary from database"""

        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session()

    def delete(self, obj=None):
        """
        pub instance methond that deletes obj from objects if inside
        """
        if obj is None:
            return
        self.__session.delete(obj)

    def close(self):
        self.__session.close()
