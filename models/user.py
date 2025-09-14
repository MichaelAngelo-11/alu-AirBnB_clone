#!/usr/bin/env python3
"""User model module."""

from models.base_model import BaseModel


class User(BaseModel):
    """User class inheriting from BaseModel."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
