#!/usr/bin/env python3
"""Unit tests for State model."""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for the State class."""

    def test_name_attribute(self):
        obj = State()
        self.assertEqual(obj.name, "")


if __name__ == "__main__":
    unittest.main()
