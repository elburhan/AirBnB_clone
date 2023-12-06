#!/usr/bin/python3
"""
Defines the Amenity class.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Represents an Amenity for the HBnB project.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new Amenity.

        Args:
            *args: Unused.
            **kwargs: Key/value pairs of attributes.
        """
        super().__init__(*args, **kwargs)
        self.name = ""  # empty string
