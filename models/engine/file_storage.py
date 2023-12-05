#!/usr/bin/python3
"""
This module serializes the python instance into JSON file
and deserializes the JSON file into class instance as necessary.
"""


import json


class FileStorage:
    """
    Class to manage serialization and deserialization
    of the project data
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the __objects instance
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        classname = obj.__class__.__name__
        object_key = str(classname + "." + obj.id)
        self.__objects[object_key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        from models.base_model import BaseModel
        filename = self.__file_path
        with open(filename, "w", encoding="UTF-8") as file:
            serialized_objects = {
                key: value.__dict__ if isinstance(value, BaseModel) else value
                for key, value in self.__objects.items()
            }
            json.dump(serialized_objects, file, default=str)

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
                self.__objects = json.load(file)
                return self.__objects
        except FileNotFoundError:
            return
