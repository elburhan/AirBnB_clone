#!/usr/bin/python3
"""
This module contains the User class
that inherits from BaseModel
"""


from models.base_model import BaseModel
#from . import storage


class User(BaseModel):
    """
    This class contains all the unique attributes of the user class
    and inherits the attributes of the BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
