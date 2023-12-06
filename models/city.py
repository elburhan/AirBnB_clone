#!/usr/bin/python3
"""
Defines the City class.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Represents a City for the HBnB project.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new City.

        Args:
            *args: Unused.
            **kwargs: Key/value pairs of attributes.
        """
        super().__init__(*args, **kwargs)
        self.state_id = ""  # empty string
        self.name = ""  # empty string
