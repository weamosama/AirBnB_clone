#!/usr/bin/python3

"""Defines unittests for models/amenity.py.
Unittest classes:
    TestAmenity_instantiation
    TestAmenity_save
    TestAmenity_to_dict
"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    def test_inheritance(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)

    def test_attributes(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_str_representation(self):
        amenity = Amenity()
        amenity.id = "789"
        self.assertEqual(str(amenity), "[Amenity] (789) {}")


if __name__ == '__main__':
    unittest.main()
