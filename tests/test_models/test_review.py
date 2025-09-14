#!/usr/bin/env python3
"""Unit tests for Review model."""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for the Review class."""

    def test_attributes_exist(self):
        obj = Review()
        self.assertTrue(hasattr(obj, "place_id"))
        self.assertTrue(hasattr(obj, "user_id"))
        self.assertTrue(hasattr(obj, "text"))


if __name__ == "__main__":
    unittest.main()
