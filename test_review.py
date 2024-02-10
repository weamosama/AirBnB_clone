#!/usr/bin/python3
"""Defines unittests for models/review.py.
Unittest classes:
    TestReview_instantiation
    TestReview_save
    TestReview_to_dict
"""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    def test_inheritance(self):
        review = Review()
        self.assertIsInstance(review, BaseModel)

    def test_attributes(self):
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_str_representation(self):
        review = Review()
        review.id = "202"
        self.assertEqual(str(review), "[Review] (202) {}")


if __name__ == '__main__':
    unittest.main()
