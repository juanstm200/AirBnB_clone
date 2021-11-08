#!/usr/bin/python3
""" tests """

import unittest
import re
from models.base_model import *
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """ Unittest for BaseModel class """

    def test_createAttr_noArgs(self):
        """ Check for create an instance """
        my_model = BaseModel()
        my_model.name = "Holberton"
        self.assertEqual(my_model.name, "Holberton")

    def test_id_noArgs(self):
        """ Check for id value """
        my_model = BaseModel()
        self.assertTrue(my_model.id)
        self.assertEqual(type(my_model.id), str)

    def test_created_at_noArgs_type(self):
        """ Check type of created_at """
        my_model = BaseModel()
        self.assertEqual(type(my_model.created_at), datetime)

    def test_created_at_noArgs_format(self):
        """ Check for datetime """
        datetime_format = re.compile(
            "\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d+$")
        my_model = BaseModel()
        my_created_at = my_model.to_dict()['created_at']
        format_found = datetime_format.match(my_created_at)
        self.assertIsNotNone(format_found)

    def test_created_at_noArgs_value(self):
        """ Check value of created_at w/o args"""
        now = datetime.now().replace(microsecond=0)
        my_model = BaseModel()
        self.assertEqual(my_model.created_at.replace(microsecond=0), now)

    def test_created_at_noArgs_afterSave(self):
        """ check created_at w/o args after save() """
        my_model = BaseModel()
        my_created_at = my_model.created_at
        my_model.save()
        self.assertEqual(my_model.created_at, my_created_at)

    def test_updated_at_noArgs_type(self):
        """ Check type updated_at """
        my_model = BaseModel()
        self.assertEqual(type(my_model.updated_at), datetime)

    def test_updated_at_noArgs_format(self):
        """ Check for ISO format """
        datetime_format = re.compile(
            "\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d+$")
        my_model = BaseModel()
        my_updated_at = my_model.to_dict()['updated_at']
        format_found = datetime_format.match(my_updated_at)
        self.assertIsNotNone(format_found)

    def test_updated_at_noArgs_value(self):
        """ check value of updated_at """
        now = datetime.now().replace(microsecond=0)
        my_model = BaseModel()
        self.assertEqual(my_model.updated_at.replace(microsecond=0), now)

    def test_updated_at_noArgs_value_afterSave(self):
        """ Check value of updated_at after save() """
        my_model = BaseModel()
        updated_pre = my_model.updated_at
        my_model.save()
        self.assertTrue(my_model.updated_at > updated_pre)

    def test_str(self):
        """ Check __str__ method """
        my_model = BaseModel()
        r = re.compile("\[BaseModel\] (.*) {.*}")
        my_str = my_model.__str__()
        self.assertIsNotNone(r.match(my_str))

    def test_to_dict_noAditonalAttr(self):
        """ Check to_dict w/o additional Attributes """
        my_model = BaseModel()
        BaseModel.name = "holberton"
        attributes = {}
        for key, value in my_model.to_dict().items():
            if (key not in ('__class__', 'id', 'created_at', 'updated_at')):
                attributes[key] = value
        self.assertFalse(attributes)

if __name__ == '__main__':
    unittest.main()
