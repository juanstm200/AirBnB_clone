#!/usr/bin/python3
"""
The class User which inherits from the class BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """ Initialization of the class attributes """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    email = ""
    password = ""
    first_name = ""
    last_name = ""
