#!/usr/bin/python3
"""
Defines the City class.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Represents a City for the HBnB project.
    """
    state_id = ""  # empty string
    name = ""  # empty string
