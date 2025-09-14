#!/usr/bin/env python3
"""Unit tests for BaseModel."""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def test_instance_creation(self):
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)
        self.assertTrue(hasattr(obj, "id"))
        self.assertTrue(hasattr(obj, "created_at"))
        self.assertTrue(hasattr(obj, "updated_at"))

    def test_save_updates_updated_at(self):
        obj = BaseModel()
        old_time = obj.updated_at
        obj.save()
        self.assertNotEqual(old_time, obj.updated_at)

    def test_to_dict_contains_class(self):
        obj = BaseModel()
        d = obj.to_dict()
        self.assertEqual(d["__class__"], "BaseModel")
        self.assertIn("created_at", d)
        self.assertIn("updated_at", d)


if __name__ == "__main__":
    unittest.main()
