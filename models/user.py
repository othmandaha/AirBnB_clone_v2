#!/usr/bin/python3
"""This module defines a class User"""
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        email = Column(String(128), nullable=False)
    else:
        email = ''

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        password = Column(String(128), nullable=False)    
    else:
        password = ''
    
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        first_name = Column(String(128), nullable=True)    
    else:
        first_name = ''

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        last_name = Column(String(128), nullable=True)
    else:
        last_name = ''
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        places = relationship('Place',cascade="all, delete, delete-orphan",
                              backref='user')
    else:
        place = None
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review',cascade="all, delete, delete-orphan",
                               backref='user')
    else:
        reviews = None
