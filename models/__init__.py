#!/usr/bin/env python3
"""models package init: exposes a storage singleton."""

from models.engine.file_storage import FileStorage  # noqa: E402

storage = FileStorage()
# Optionally, import classes here when available to pass to reload
# from models.base_model import BaseModel  # noqa: F401,E402
# storage.reload({"BaseModel": BaseModel})
