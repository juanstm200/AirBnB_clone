#!/usr/bin/python3
"""
The class Review which inherits from the class BaseModel
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Initialization of the class attributes"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    place_id = ""
    user_id = ""
    text = ""
