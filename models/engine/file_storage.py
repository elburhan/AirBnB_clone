#!/usr/bin/python3
"""
This module serializes the Python instance into a JSON file
and deserializes the JSON file into class instances as necessary.
"""

import json
import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    """
    Class to manage serialization and deserialization
    of the project data
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the __objects dictionary that contains all
            the instances of the class ... and previous saved.
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        classname = type(obj).__name__
        object_key = str(classname + "." + obj.id)
        self.__objects[object_key] = obj

    def save(self):
        """
        serializes __objects dictionary to the JSON file (path: __file_path)
        """
        filename = self.__file_path
        with open(filename, "w", encoding="UTF-8") as file:
            serialized_objects = {key: value.to_dict() for key, value in self.__objects.items()}
            json.dump(serialized_objects, file)

    def classes(self):
        """Returns a dictionary of valid classes and their references"""
        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }
        return classes

    def reload(self):
        """
        deserializes the JSON file to __objects 
        (only if the JSON file (__file_path) exists
        otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        filename = self.__file_path
        try:
            with open(filename, "r", encoding="UTF-8") as file:
                if not file:
                    return
                obj_dict = json.load(file)
                obj_dict = {k: self.classes()[v["__class__"]](**v) for k, v in obj_dict.items()}
                self.__objects = obj_dict
                return self.__objects
        except:
            return

    def attributes(self):
        """Returns the valid attributes and their types for classname"""
        attributes = {
            "BaseModel": {"id": str, "created_at": datetime.datetime, "updated_at": datetime.datetime},
            "User": {"email": str, "password": str, "first_name": str, "last_name": str},
            "State": {"name": str},
            "City": {"state_id": str, "name": str},
            "Amenity": {"name": str},
            "Place": {"city_id": str, "user_id": str, "name": str, "description": str,
                      "number_rooms": int, "number_bathrooms": int, "max_guest": int,
                      "price_by_night": int, "latitude": float, "longitude": float, "amenity_ids": list},
            "Review": {"place_id": str, "user_id": str, "text": str}
        }
        return attributes
