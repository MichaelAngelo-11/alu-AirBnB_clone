#!/usr/bin/env python3
"""Unit tests for User model."""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for the User class."""

    def test_attributes_exist(self):
        obj = User()
        self.assertTrue(hasattr(obj, "email"))
        self.assertTrue(hasattr(obj, "password"))
        self.assertTrue(hasattr(obj, "first_name"))
        self.assertTrue(hasattr(obj, "last_name"))


if __name__ == "__main__":
    unittest.main()
