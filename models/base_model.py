#!/usr/bin/python3
"""
In this module, the base class BaseModel
"""

import uuid
import models
from datetime import datetime


class BaseModel():
    """ Creating the Base class """

    def __init__(self, *args, **kwargs):
        """ Initialization of the instance """

        current_time = datetime.now()
        if kwargs != {}:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                else:
                    if key == 'created_at' or key == 'updated_at':
                        str_Var = "%Y-%m-%dT%H:%M:%S.%f"
                        value = datetime.strptime(value, str_Var)
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = current_time
            self.updated_at = current_time
            models.storage.new(self)

    def update_instance(self, attribute, value):
        """ Add a new attribute or update instance from input """

        setattr(self, attribute, value)

    def __str__(self):
        """ Prints a representation of an instance """
        names = self.__class__.__name__
        return ("[{:s}] ({:s}) {}".format(names, self.id, self.__dict__))

    def save(self):
        """ Updates the public instance attribute """

        current_time_updated = datetime.now()
        self.updated_at = current_time_updated
        models.storage.save()

    def to_dict(self):
        """ Returns a dictionary of the instance """

        objects_dict = self.__dict__.copy()
        objects_dict.update({'__class__': self.__class__.__name__,
                             'created_at': self.created_at.isoformat(),
                             'updated_at': self.updated_at.isoformat()})
        return objects_dict
