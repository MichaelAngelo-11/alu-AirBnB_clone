#!/usr/bin/env python3
"""City model module."""

from models.base_model import BaseModel


class City(BaseModel):
    """City class inheriting from BaseModel."""

    state_id = ""
    name = ""
