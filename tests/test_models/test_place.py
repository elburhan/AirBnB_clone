import unittest
from models.place import Place
from datetime import datetime
import os
import json


class TestPlace(unittest.TestCase):
    """
    Test the Place class
    """
    def test_init(self):
        """
        Test the initialization of the Place
        """
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertTrue(hasattr(place, 'id'))
        self.assertTrue(hasattr(place, 'created_at'))
        self.assertTrue(hasattr(place, 'updated_at'))
        self.assertEqual(type(place.id), str)
        self.assertEqual(type(place.created_at), datetime)
        self.assertEqual(type(place.updated_at), datetime)
        self.assertEqual(place.city_id, '')
        self.assertEqual(place.user_id, '')
        self.assertEqual(place.name, '')
        self.assertEqual(place.description, '')
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_str(self):
        """
        Test the __str__ method of the Place
        """
        place = Place()
        string_representation = str(place)
        self.assertIn('[Place]', string_representation)
        self.assertIn('id', string_representation)
        self.assertIn('created_at', string_representation)
        self.assertIn('updated_at', string_representation)

    def test_save(self):
        """
        Test the save method of the Place
        """
        place = Place()
        original_updated_at = place.updated_at
        place.save()
        self.assertNotEqual(original_updated_at, place.updated_at)

    def test_to_dict(self):
        """
        Test the to_dict method of the Place
        """
        place = Place()
        place_dict = place.to_dict()
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertEqual(type(place_dict['created_at']), str)
        self.assertEqual(type(place_dict['updated_at']), str)
        self.assertEqual(place_dict['city_id'], '')
        self.assertEqual(place_dict['user_id'], '')
        self.assertEqual(place_dict['name'], '')
        self.assertEqual(place_dict['description'], '')
        self.assertEqual(place_dict['number_rooms'], 0)
        self.assertEqual(place_dict['number_bathrooms'], 0)
        self.assertEqual(place_dict['max_guest'], 0)
        self.assertEqual(place_dict['price_by_night'], 0)
        self.assertEqual(place_dict['latitude'], 0.0)
        self.assertEqual(place_dict['longitude'], 0.0)
        self.assertEqual(place_dict['amenity_ids'], [])

    def test_to_dict_with_args(self):
        """
        Test the to_dict method of the Place with additional arguments
        """
        place = Place(
            id='123',
            created_at=datetime.now(),
            updated_at=datetime.now(),
            city_id='456',
            user_id='789',
            name='Example Place',
            description='This is an example place',
            number_rooms=2,
            number_bathrooms=1,
            max_guest=4,
            price_by_night=100,
            latitude=12.34,
            longitude=-56.78,
            amenity_ids=['a1', 'a2']
        )
        place_dict = place.to_dict()
        self.assertEqual(place_dict['id'], '123')
        self.assertEqual(type(place_dict['created_at']), str)
        self.assertEqual(type(place_dict['updated_at']), str)
        self.assertEqual(place_dict['city_id'], '456')
        self.assertEqual(place_dict['user_id'], '789')
        self.assertEqual(place_dict['name'], 'Example Place')
        self.assertEqual(place_dict['description'], 'This is an example place')
        self.assertEqual(place_dict['number_rooms'], 2)
        self.assertEqual(place_dict['number_bathrooms'], 1)
        self.assertEqual(place_dict['max_guest'], 4)
        self.assertEqual(place_dict['price_by_night'], 100)
        self.assertEqual(place_dict['latitude'], 12.34)
        self.assertEqual(place_dict['longitude'], -56.78)
        self.assertEqual(place_dict['amenity_ids'], ['a1', 'a2'])

    def test_to_dict_and_back(self):
        """
        Test if a Place instance can be recreated from its to_dict representation
        """
        place = Place()
        place_dict = place.to_dict()
        new_place = Place(**place_dict)
        self.assertEqual(place.to_dict(), new_place.to_dict())

    def tearDown(self):
        """
        Clean up: Remove the JSON file created during tests
        """
        try:
            os.remove('Place.json')
        except FileNotFoundError:
            pass


if __name__ == '__main__':
    unittest.main()
