#!/usr/bin/python3
"""
The class State which inherits from the class BaseModel
"""

from models.base_model import BaseModel


class State(BaseModel):
    """ Initialization of the class attributes """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    name = ""
