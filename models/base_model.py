#!/usr/bin/env python3
"""
BaseModel for alu-AirBnB_clone.

Provides id, created_at, updated_at, to_dict, save, and __str__.
"""
from datetime import datetime
import uuid


ISO_FMT = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """Base class that other classes will inherit from."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance.

        If kwargs is provided, initialize from dictionary (as from
        storage). Otherwise, create a new instance with new id/time.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.strptime(value, ISO_FMT)
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(value, ISO_FMT)
                else:
                    setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Return a readable string representation."""
        cls = self.__class__.__name__
        return "[{}] ({}) {}".format(cls, self.id, self.__dict__)

    def save(self):
        """Update updated_at and send to storage for saving."""
        self.updated_at = datetime.now()
        try:
            # avoid circular import at module top-level
            from models import storage  # noqa: WPS433
        except Exception:
            # If storage not available, do nothing
            return
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Return a dict representation with ISO datetime strings."""
        result = dict(self.__dict__)
        result["__class__"] = self.__class__.__name__
        if hasattr(self, "created_at"):
            result["created_at"] = self.created_at.strftime(ISO_FMT)
        if hasattr(self, "updated_at"):
            result["updated_at"] = self.updated_at.strftime(ISO_FMT)
        return result
