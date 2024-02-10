#!/usr/bin/python3
"""Defines unittests for models/state.py.
Unittest classes:
    TestState_instantiation
    TestState_save
    TestState_to_dict
"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    def test_inheritance(self):
        state = State()
        self.assertIsInstance(state, BaseModel)

    def test_attributes(self):
        state = State()
        self.assertEqual(state.name, "")

    def test_str_representation(self):
        state = State()
        state.id = "123"
        self.assertEqual(str(state), "[State] (123) {}")


if __name__ == '__main__':
    unittest.main()
