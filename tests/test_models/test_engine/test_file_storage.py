#!/usr/bin/env python3
"""Unit tests for FileStorage engine."""

import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    def setUp(self):
        """Setup a fresh FileStorage before each test."""
        self.storage = FileStorage()
        self.test_file = "file.json"
        # ensure no leftover file
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def tearDown(self):
        """Clean up JSON file after each test."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_all_returns_dict(self):
        self.assertIsInstance(self.storage.all(), dict)

    def test_new_and_save(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.assertTrue(os.path.exists(self.test_file))

    def test_reload(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload({"BaseModel": BaseModel})
        key = "BaseModel.{}".format(obj.id)
        self.assertIn(key, self.storage.all())


if __name__ == "__main__":
    unittest.main()
