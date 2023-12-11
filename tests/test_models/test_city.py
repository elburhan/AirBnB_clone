import unittest
from models.city import City
from datetime import datetime
import os
import json


class TestCity(unittest.TestCase):
    """
    Test the City class
    """
    def test_init(self):
        """
        Test the initialization of the City
        """
        city = City()
        self.assertIsInstance(city, City)
        self.assertTrue(hasattr(city, 'id'))
        self.assertTrue(hasattr(city, 'created_at'))
        self.assertTrue(hasattr(city, 'updated_at'))
        self.assertEqual(type(city.id), str)
        self.assertEqual(type(city.created_at), datetime)
        self.assertEqual(type(city.updated_at), datetime)
        self.assertEqual(city.state_id, '')
        self.assertEqual(city.name, '')

    def test_str(self):
        """
        Test the __str__ method of the City
        """
        city = City()
        string_representation = str(city)
        self.assertIn('[City]', string_representation)
        self.assertIn('id', string_representation)
        self.assertIn('created_at', string_representation)
        self.assertIn('updated_at', string_representation)

    def test_save(self):
        """
        Test the save method of the City
        """
        city = City()
        original_updated_at = city.updated_at
        city.save()
        self.assertNotEqual(original_updated_at, city.updated_at)

    def test_to_dict(self):
        """
        Test the to_dict method of the City
        """
        city = City()
        city_dict = city.to_dict()
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertEqual(type(city_dict['created_at']), str)
        self.assertEqual(type(city_dict['updated_at']), str)
        self.assertEqual(city_dict['state_id'], '')
        self.assertEqual(city_dict['name'], '')

    def test_to_dict_with_args(self):
        """
        Test the to_dict method of the City with additional arguments
        """
        city = City(id='123', created_at=datetime.now(), updated_at=datetime.now(), state_id='456', name='Example City')
        city_dict = city.to_dict()
        self.assertEqual(city_dict['id'], '123')
        self.assertEqual(type(city_dict['created_at']), str)
        self.assertEqual(type(city_dict['updated_at']), str)
        self.assertEqual(city_dict['state_id'], '456')
        self.assertEqual(city_dict['name'], 'Example City')

    def test_to_dict_and_back(self):
        """
        Test if a City instance can be recreated from its to_dict representation
        """
        city = City()
        city_dict = city.to_dict()
        new_city = City(**city_dict)
        self.assertEqual(city.to_dict(), new_city.to_dict())

    def tearDown(self):
        """
        Clean up: Remove the JSON file created during tests
        """
        try:
            os.remove('City.json')
        except FileNotFoundError:
            pass


if __name__ == '__main__':
    unittest.main()
