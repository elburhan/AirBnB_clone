#!/usr/bin/python3
"""
This module serializes the python instance into JSON file
and deserializes the JSON file into class instance as necessary.
"""


import JSON


class FileStorage:
    """
    Class to manage serialization and deserialization
    of the project data
    """
    self.__file_path = file.json
    self.__objects = {}

    def all(self):
        """
        returns the __objects instance
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        classname = __class__.__name__
        object_key = str(classname + "." + self.id)
        self.__objects[object_key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        filename = self.__file_path
        with open(filename, "a", encoding="UTF-8") as file:
            file.write(json.dumps(self.__objects))

    def reload(self):
        """
        deserializes the JSON file to __objects 
        (only if the JSON file (__file_path) exists
        otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        filename = self.__file_path
        try:
            with open(filename, "r") as file:
                self.__objects = json.load(file)
        except FileNotFoundError:
            return
