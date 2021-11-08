#!/usr/bin/python3
"""
In this module the class City which inherits from the class BaseModel
"""

from models.base_model import BaseModel


class City(BaseModel):
    """ Initialization of the class attributes """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    state_id = ""
    name = ""
