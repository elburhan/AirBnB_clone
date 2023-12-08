#!/usr/bin/python3
"""
Defines the Review class.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Represents a Review for the HBnB project.
    """
    place_id = ""  # empty string
    user_id = ""  # empty string
    text = ""  # empty string
