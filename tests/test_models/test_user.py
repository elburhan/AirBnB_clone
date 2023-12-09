import unittest
from models.user import User
from datetime import datetime
import os
import json


class TestUser(unittest.TestCase):
    """
    Test the User class
    """
    def test_init(self):
        """
        Test the initialization of the User
        """
        user = User()
        self.assertIsInstance(user, User)
        self.assertTrue(hasattr(user, 'id'))
        self.assertTrue(hasattr(user, 'created_at'))
        self.assertTrue(hasattr(user, 'updated_at'))
        self.assertEqual(type(user.id), str)
        self.assertEqual(type(user.created_at), datetime)
        self.assertEqual(type(user.updated_at), datetime)
        self.assertEqual(user.email, '')
        self.assertEqual(user.password, '')
        self.assertEqual(user.first_name, '')
        self.assertEqual(user.last_name, '')

    def test_str(self):
        """
        Test the __str__ method of the User
        """
        user = User()
        string_representation = str(user)
        self.assertIn('[User]', string_representation)
        self.assertIn('id', string_representation)
        self.assertIn('created_at', string_representation)
        self.assertIn('updated_at', string_representation)

    def test_save(self):
        """
        Test the save method of the User
        """
        user = User()
        original_updated_at = user.updated_at
        user.save()
        self.assertNotEqual(original_updated_at, user.updated_at)

    def test_to_dict(self):
        """
        Test the to_dict method of the User
        """
        user = User()
        user_dict = user.to_dict()
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(type(user_dict['created_at']), str)
        self.assertEqual(type(user_dict['updated_at']), str)
        self.assertEqual(user_dict['email'], '')
        self.assertEqual(user_dict['password'], '')
        self.assertEqual(user_dict['first_name'], '')
        self.assertEqual(user_dict['last_name'], '')

    def test_to_dict_with_args(self):
        """
        Test the to_dict method of the User with additional arguments
        """
        user = User(
            id='123',
            created_at=datetime.now(),
            updated_at=datetime.now(),
            email='user@example.com',
            password='securepassword',
            first_name='John',
            last_name='Doe'
        )
        user_dict = user.to_dict()
        self.assertEqual(user_dict['id'], '123')
        self.assertEqual(type(user_dict['created_at']), str)
        self.assertEqual(type(user_dict['updated_at']), str)
        self.assertEqual(user_dict['email'], 'user@example.com')
        self.assertEqual(user_dict['password'], 'securepassword')
        self.assertEqual(user_dict['first_name'], 'John')
        self.assertEqual(user_dict['last_name'], 'Doe')

    def test_to_dict_and_back(self):
        """
        Test if a User instance can be recreated from its to_dict representation
        """
        user = User()
        user_dict = user.to_dict()
        new_user = User(**user_dict)
        self.assertEqual(user.to_dict(), new_user.to_dict())

    def tearDown(self):
        """
        Clean up: Remove the JSON file created during tests
        """
        try:
            os.remove('User.json')
        except FileNotFoundError:
            pass


if __name__ == '__main__':
    unittest.main()
