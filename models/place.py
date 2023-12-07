#!/usr/bin/python3
"""
Defines the Place class.
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Represents the place class for the HBnB project
    """
    city_id = ""  # empty string
    user_id = ""  # empty string
    name = ""  # empty string
    description = ""  # empty string
    number_rooms = 0  # integer - 0
    number_bathrooms = 0  # integer - 0
    max_guest = 0  # integer - 0
    price_by_night = 0  # integer - 0
    latitude = 0.0  # float - 0.0
    longitude = 0.0  # float - 0.0
    amenity_ids = []  # list of string - empty list
>>>>>>> main
