#!/usr/bin/python3
"""
Class Amenity which inherits form the class BaseModel
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Initialization of the class attributes """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    name = ""
