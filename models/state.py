#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv

class State(BaseModel, Base):
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE", None) != "db":
        @property
        def cities(self):
            """List of cities"""
            from models import storage
            cities_list = []
            all_cities = storage.all(City).values()
            for city in all_cities:
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
