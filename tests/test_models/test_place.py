#!/usr/bin/env python3
"""Unit tests for Place model."""

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test cases for the Place class."""

    def test_default_attributes(self):
        obj = Place()
        self.assertEqual(obj.number_rooms, 0)
        self.assertEqual(obj.number_bathrooms, 0)
        self.assertEqual(obj.max_guest, 0)
        self.assertEqual(obj.price_by_night, 0)
        self.assertIsInstance(obj.amenity_ids, list)


if __name__ == "__main__":
    unittest.main()
