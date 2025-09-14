#!/usr/bin/env python3
"""Unit tests for City model."""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for the City class."""

    def test_attributes_exist(self):
        obj = City()
        self.assertTrue(hasattr(obj, "state_id"))
        self.assertTrue(hasattr(obj, "name"))


if __name__ == "__main__":
    unittest.main()
