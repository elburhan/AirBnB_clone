#!/usr/bin/python3
"""
Defines the Review class.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Represents a Review for the HBnB project.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new Review.

        Args:
            *args: Unused.
            **kwargs: Key/value pairs of attributes.
        """
        super().__init__(*args, **kwargs)
        self.place_id = ""  # empty string
        self.user_id = ""  # empty string
        self.text = ""  # empty string
