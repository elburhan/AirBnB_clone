#!/usr/bin/python3
"""
The base model for all the other classes in the Project.
"""


import datetime
import uuid


class BaseModel:
    """
    This is the class for managing all common attributes for the 
    project
    """
    def __init__(self, id=None, updated_at=None, name=None):
        self.id  = str(uuid.uuid4())
        self.created_at = str(datetime.datetime())
        self.updated_at = updated_at
        self.name = name

    def __str__(self):
        """
        updates the __str__ function
        """
        return (f"[{self.name}] ({self.id}) {self.__dict__}")
    
    def save(self):
        self.updated_at = str(datetime.datetime())

    def to_dict(self):
        pass