#!/usr/bin/python3
"""
initialization module for the model package
"""

from models.engine.file_storage import FileStorage


storage = FileStorage()

storage.reload()
