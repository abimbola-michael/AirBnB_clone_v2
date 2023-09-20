#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy import relationship


place_amenity = Table('place_amenity', Base.metadata, nullable=False,
        Column('place_id', String(60), ForeignKey('place_id'), primary_key=True),
        Column('amenity_id', String(60),
            ForeignKey('amenities.id'), nullable=False, primary_key=True))


class Place(BaseModel):
    """ A place to stay """
    city_id = Column(String(60), nullable=False, ForeignKey('cities.id'))
    user_id =  Column(String(60), nullable=False, ForeignKey('users.id'))
    name =  Column(String(128), nullable=False)
    description =  Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night =Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity = relationship("Amenity", secondary=place_amenity, viewonly=False)
    reviews = relationship("Reviews", backref='place', cascade="all, delete")
