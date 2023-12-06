#!/usr/bin/python3
"""
Defines the State class.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Represents a State for the HBnB project.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new State.

        Args:
            *args: Unused.
            **kwargs: Key/value pairs of attributes.
        """
        super().__init__(*args, **kwargs)
        self.name = ""  # empty string
