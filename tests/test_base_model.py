#!/usr/bin/python3
"""
Unittests for BaseModel class
"""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test cases for BaseModel class
    """

    def test_attributes(self):
        """
        Test the attributes of BaseModel instance
        """
        my_model = BaseModel()
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_save(self):
        """
        Test the save method of BaseModel
        """
        my_model = BaseModel()
        original_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(original_updated_at, my_model.updated_at)

    def test_to_dict(self):
        """
        Test the to_dict method of BaseModel
        """
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()

        self.assertIsInstance(my_model_json, dict)
        self.assertEqual(my_model_json['__class__'], 'BaseModel')
        self.assertEqual(my_model_json['name'], 'My First Model')
        self.assertEqual(my_model_json['my_number'], 89)
        self.assertIn('created_at', my_model_json)
        self.assertIn('updated_at', my_model_json)


if __name__ == "__main__":
    unittest.main()
