#!/usr/bin/python3
"""
Defines unit tests for the Amenity class.
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Test cases for the Amenity class.
    """

    def test_instance_creation(self):
        """
        Test that an instance of Amenity is correctly created.
        """
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity, BaseModel)

    def test_attributes(self):
        """
        Test that the attributes of Amenity are correctly set.
        """
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_str_representation(self):
        """
        Test that the __str__ method returns the expected string.
        """
        amenity = Amenity()
        string_repr = str(amenity)
        self.assertIn("[Amenity]", string_repr)
        self.assertIn("'id':", string_repr)
        self.assertIn("'created_at':", string_repr)
        self.assertIn("'updated_at':", string_repr)

    def test_to_dict_method(self):
        """
        Test that the to_dict method returns a dictionary with expected keys/values.
        """
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertEqual(amenity_dict['name'], "")
        self.assertIn('id', amenity_dict)
        self.assertIn('created_at', amenity_dict)
        self.assertIn('updated_at', amenity_dict)


if __name__ == '__main__':
    unittest.main()
