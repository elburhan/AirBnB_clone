#!/usr/bin/python3
"""
Test module for BaseModel class.
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
from unittest.mock import patch
import os


class TestBaseModel(unittest.TestCase):
    """
    Test cases for BaseModel class.
    """

    def test_instance_creation(self):
        """
        Test instance creation and attributes.
        """
        model = BaseModel()
        self.assertTrue(isinstance(model, BaseModel))
        self.assertTrue(hasattr(model, 'id'))
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertTrue(hasattr(model, 'updated_at'))

    def test_instance_creation_with_id(self):
        """
        Test instance creation with provided id.
        """
        model = BaseModel(id="test_id")
        self.assertEqual(model.id, "test_id")

    def test_instance_creation_with_created_at(self):
        """
        Test instance creation with provided created_at.
        """
        date_str = "2023-12-05T14:30:00"
        model = BaseModel(created_at=date_str)
        expected_date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S")
        self.assertEqual(model.created_at, expected_date)

    def test_instance_creation_with_updated_at(self):
        """
        Test instance creation with provided updated_at.
        """
        date_str = "2023-12-05T14:30:00"
        model = BaseModel(updated_at=date_str)
        expected_date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S")
        self.assertEqual(model.updated_at, expected_date)

    def test_instance_creation_with_attributes(self):
        """
        Test instance creation with additional attributes.
        """
        model = BaseModel(name="Test", value=42)
        self.assertTrue(hasattr(model, 'name'))
        self.assertTrue(hasattr(model, 'value'))
        self.assertEqual(model.name, "Test")
        self.assertEqual(model.value, 42)

    def test_save_method(self):
        """
        Test save method.
        """
        model = BaseModel()
        with patch('models.storage') as mock_storage:
            model.save()
            mock_storage.save.assert_called_once()

    def test_to_dict_method(self):
        """
        Test to_dict method.
        """
        date_str = "2023-12-05T14:30:00"
        model = BaseModel(id="test_id", created_at=date_str, updated_at=date_str, name="Test", value=42)
        expected_dict = {
            '__class__': 'BaseModel',
            'id': 'test_id',
            'created_at': date_str,
            'updated_at': date_str,
            'name': 'Test',
            'value': 42
        }
        self.assertEqual(model.to_dict(), expected_dict)

    def test_str_method(self):
        """
        Test __str__ method.
        """
        model = BaseModel(id="test_id", name="Test", value=42)
        expected_str = "[BaseModel] (test_id) {'id': 'test_id', 'name': 'Test', 'value': 42}"
        self.assertEqual(str(model), expected_str)


if __name__ == '__main__':
    unittest.main()