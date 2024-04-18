#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Representation of Amenity """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    places = relationship("Place", secondary="place_amenity",
                              back_populates="amenities")