#!/usr/bin/python3
"""Defines unittests for models/city.py.
Unittest classes:
    TestCity_instantiation
    TestCity_save
    TestCity_to_dict
"""

import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    def test_inheritance(self):
        city = City()
        self.assertIsInstance(city, BaseModel)

    def test_attributes(self):
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_str_representation(self):
        city = City()
        city.id = "456"
        self.assertEqual(str(city), "[City] (456) {}")


if __name__ == '__main__':
    unittest.main()
