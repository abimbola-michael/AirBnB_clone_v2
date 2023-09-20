#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from os import getenv
from models.review import Review
from models.amenity import Amenity


place_amenity = Table('place_amenity', Base.metadata, Column(
    'place_id', String(60), ForeignKey('places.id'), primary_key=True), Column(
        'amenity_id', String(60), ForeignKey(
            'amenities.id'), nullable=False, primary_key=True))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenities = relationship(
            "Amenity", secondary="place_amenity", viewonly=False)
    reviews = relationship("Review", backref='place', cascade="all, delete")

    if getenv("HBNB_TYPE_STORAGE", None) != "db":
        @property
        def reviews(self):
            """List of reviews"""
            from models import storage
            reviews_list = []
            all_reviews = storage.all(Review).values()
            for review in all_reviews:
                if review.place_id == self.id:
                    reviews_list.append(review)
            return reviews_list

        @property
        def amenities(self):
            """List of amenities"""
            from models import storage
            amenties_list = []
            all_amenities = storage.all(Amenity).values()
            for amenity in all_amenities:
                if amenity.id == self.id:
                    amenities_list.append(amenity)
            return amenities_list
