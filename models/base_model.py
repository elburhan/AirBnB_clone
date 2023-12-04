#!/usr/bin/python3
"""
The base model for all the other classes in the Project.
"""


from datetime import datetime
import uuid


class BaseModel:
    """
    This is the class for managing all common attributes for the 
    project
    """
    def __init__(self):
        self.id  = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.name = None

    def __str__(self):
        """
        updates the __str__ function
        """
        return (f"[{__class__.__name__}] ({self.id}) {self.__dict__}")
    
    def save(self):
        """
        Saves the information of the class to a file
        and updates the updated_at
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        This method updates the __dict__ method with:
        __class__(str): classname
        updated_at(str)
        created_at(str)
        """
        dictionary = self.__dict__
        dictionary["__class__"] = __class__.__name__
        dictionary["updated_at"] = str(self.updated_at)
        dictionary["created_at"] = str(self.created_at)
        return dictionary

