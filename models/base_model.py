#!/usr/bin/python3
"""
The base model for all the other classes in the Project.
"""

from datetime import datetime
import uuid
from models import storage


class BaseModel:
    """
    This is the class for managing all common attributes for the 
    project
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new basemodel with created_at and unique id.
        it takes two arguments
        *args: unused
        **kwargs: a dictionary of attibutes and value pairs to assign in the new
                    basemodel.
        """
        if kwargs is not None and kwargs != {}:
            # if a dictionary was passed to <kwargs>
            # update the class dictionary <__dict__> with the newly created object dictionary
            # And the dictionary passed <kwargs>
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ["created_at", "updated_at"]:
                    self.__dict__[key] = datetime.strptime(
                        kwargs[key], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id  = str(uuid.uuid4()) # create a unique id
            self.created_at = datetime.now() # store the time created at
            self.updated_at = datetime.now() # update the updated at time
            storage.new(self) # creates a new object with key [<obj class name>.id]

    def __str__(self):
        """
        updates the __str__ function to print in this format
        [<class name>] (<self.id>) <self.__dict__>
        """
        return (f"[{type(self).__name__}] ({self.id}) {self.__dict__}")
    
    def save(self):
        """
        Saves the information of the class to a file
        and updates the updated_at time
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        This method updates the values in the class dictiinary <__dict__>:
        __class__(str): classname
        updated_at(isoformat)
        created_at(isoformat)
        so it can be easily converted to json format
        """
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = type(self).__name__
        dictionary["updated_at"] = self.updated_at.isoformat()
        dictionary["created_at"] = self.created_at.isoformat()
        return dictionary

