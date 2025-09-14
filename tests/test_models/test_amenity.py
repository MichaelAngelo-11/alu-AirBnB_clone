#!/usr/bin/env python3
"""Unit tests for Amenity model."""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class."""

    def test_name_default(self):
        obj = Amenity()
        self.assertEqual(obj.name, "")


if __name__ == "__main__":
    unittest.main()
