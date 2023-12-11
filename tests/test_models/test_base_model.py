import unittest
from models.base_model import BaseModel
from datetime import datetime
import os
import json


class TestBaseModel(unittest.TestCase):
    """
    Test the BaseModel class
    """
    def test_init(self):
        """
        Test the initialization of the BaseModel
        """
        base_model = BaseModel()
        self.assertIsInstance(base_model, BaseModel)
        self.assertTrue(hasattr(base_model, 'id'))
        self.assertTrue(hasattr(base_model, 'created_at'))
        self.assertTrue(hasattr(base_model, 'updated_at'))
        self.assertEqual(type(base_model.id), str)
        self.assertEqual(type(base_model.created_at), datetime)
        self.assertEqual(type(base_model.updated_at), datetime)

    def test_str(self):
        """
        Test the __str__ method of the BaseModel
        """
        base_model = BaseModel()
        string_representation = str(base_model)
        self.assertIn('[BaseModel]', string_representation)
        self.assertIn('id', string_representation)
        self.assertIn('created_at', string_representation)
        self.assertIn('updated_at', string_representation)

    def test_save(self):
        """
        Test the save method of the BaseModel
        """
        base_model = BaseModel()
        original_updated_at = base_model.updated_at
        base_model.save()
        self.assertNotEqual(original_updated_at, base_model.updated_at)

    def test_to_dict(self):
        """
        Test the to_dict method of the BaseModel
        """
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()
        self.assertEqual(base_model_dict['__class__'], 'BaseModel')
        self.assertEqual(type(base_model_dict['created_at']), str)
        self.assertEqual(type(base_model_dict['updated_at']), str)

    def test_to_dict_with_args(self):
        """
        Test the to_dict method of the BaseModel with additional arguments
        """
        base_model = BaseModel(id='123', created_at=datetime.now(), updated_at=datetime.now())
        base_model_dict = base_model.to_dict()
        self.assertEqual(base_model_dict['id'], '123')
        self.assertEqual(type(base_model_dict['created_at']), str)
        self.assertEqual(type(base_model_dict['updated_at']), str)

    def test_to_dict_and_back(self):
        """
        Test if a BaseModel instance can be recreated from its to_dict representation
        """
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()
        new_base_model = BaseModel(**base_model_dict)
        self.assertEqual(base_model.to_dict(), new_base_model.to_dict())

    def tearDown(self):
        """
        Clean up: Remove the JSON file created during tests
        """
        try:
            os.remove('BaseModel.json')
        except FileNotFoundError:
            pass


if __name__ == '__main__':
    unittest.main()
