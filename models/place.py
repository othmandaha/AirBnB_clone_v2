#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship


class Place(BaseModel):
    """ A place to stay """
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ = 'places'

        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", backref="place", cascade="all, delete-orphan")
        amenity_ids = []
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []
#Class attribute review, if dbstorage, if the Place is deleted,\
#all the review are deleted
#if filestorage, getter attribute reviews that return list of review
    if getenv("HBNB_TYPE_STORAGE") != 'db':
        @property
        def reviews(self):
            """Getter attribute that returns the list of Review instances with
            place_id equals to the current Place.id"""
            from models import storage
            reviews_list = []
            for review in storage.all("Review").values():
                if review.place_id == self.id:
                    reviews_list.append(review)
            return reviews_list
        
        @property
        def amenities(self):
            """ Getter attribute that returns the list of Amenity instances based on
            the attribute amenity_ids that contains all Amenity.id linked to the Place """
            from models.amenity import Amenity
            amenity_list = []
            all_amenities = models.storage.all(Amenity)
            for amenity in all_amenities.values():
                if amenity.place_id == self.id:
                    amenity_list.append(amenity)
            return amenity_list
