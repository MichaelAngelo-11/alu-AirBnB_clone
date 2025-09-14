#!/usr/bin/env python3
"""
Simple JSON FileStorage engine for alu-AirBnB_clone.
"""
import json
from pathlib import Path


class FileStorage:
    """Serializes instances to JSON file and deserializes back."""

    __file_path = Path("file.json")
    __objects = {}

    def all(self):
        """Return the dictionary of all stored objects."""
        return self.__class__.__objects

    def new(self, obj):
        """Add new object to storage with key <class name>.id."""
        if obj is None:
            return
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__class__.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file."""
        to_save = {}
        for key, obj in self.__class__.__objects.items():
            if hasattr(obj, "to_dict"):
                to_save[key] = obj.to_dict()
            else:
                # fallback: try to serialize __dict__
                to_save[key] = obj.__dict__
        with self.__class__.__file_path.open("w", encoding="utf-8") as fh:
            json.dump(to_save, fh, indent=2)

    def reload(self, cls_map=None):
        """Deserialize the JSON file to __objects, if file exists.

        cls_map: optional dict mapping class names to classes so we can
                 recreate real objects.
        """
        if not self.__class__.__file_path.exists():
            return
        try:
            with self.__class__.__file_path.open("r", encoding="utf-8") as fh:
                data = json.load(fh)
        except json.JSONDecodeError:
            return

        if not isinstance(data, dict):
            return

        self.__class__.__objects = {}
        for key, val in data.items():
            class_name = val.get("__class__")
            if cls_map and class_name in cls_map:
                cls = cls_map[class_name]
                self.__class__.__objects[key] = cls(**val)
            else:
                # Keep raw dict if class not available
                self.__class__.__objects[key] = val
