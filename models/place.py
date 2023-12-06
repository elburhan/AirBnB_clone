#!/usr/bin/python3
"""
Defines the Place class.
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Represents a Place for the HBnB project.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new Place.

        Args:
            *args: Unused.
            **kwargs: Key/value pairs of attributes.
        """
        super().__init__(*args, **kwargs)
        self.city_id = ""  # empty string
        self.user_id = ""  # empty string
        self.name = ""  # empty string
        self.description = ""  # empty string
        self.number_rooms = 0  # integer - 0
        self.number_bathrooms = 0  # integer - 0
        self.max_guest = 0  # integer - 0
        self.price_by_night = 0  # integer - 0
        self.latitude = 0.0  # float - 0.0
        self.longitude = 0.0  # float - 0.0
        self.amenity_ids = []  # list of string - empty list
