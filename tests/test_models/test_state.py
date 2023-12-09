import unittest
from models.state import State
from datetime import datetime
import os
import json


class TestState(unittest.TestCase):
    """
    Test the State class
    """
    def test_init(self):
        """
        Test the initialization of the State
        """
        state = State()
        self.assertIsInstance(state, State)
        self.assertTrue(hasattr(state, 'id'))
        self.assertTrue(hasattr(state, 'created_at'))
        self.assertTrue(hasattr(state, 'updated_at'))
        self.assertEqual(type(state.id), str)
        self.assertEqual(type(state.created_at), datetime)
        self.assertEqual(type(state.updated_at), datetime)
        self.assertEqual(state.name, '')

    def test_str(self):
        """
        Test the __str__ method of the State
        """
        state = State()
        string_representation = str(state)
        self.assertIn('[State]', string_representation)
        self.assertIn('id', string_representation)
        self.assertIn('created_at', string_representation)
        self.assertIn('updated_at', string_representation)

    def test_save(self):
        """
        Test the save method of the State
        """
        state = State()
        original_updated_at = state.updated_at
        state.save()
        self.assertNotEqual(original_updated_at, state.updated_at)

    def test_to_dict(self):
        """
        Test the to_dict method of the State
        """
        state = State()
        state_dict = state.to_dict()
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertEqual(type(state_dict['created_at']), str)
        self.assertEqual(type(state_dict['updated_at']), str)
        self.assertEqual(state_dict['name'], '')

    def test_to_dict_with_args(self):
        """
        Test the to_dict method of the State with additional arguments
        """
        state = State(
            id='123',
            created_at=datetime.now(),
            updated_at=datetime.now(),
            name='California'
        )
        state_dict = state.to_dict()
        self.assertEqual(state_dict['id'], '123')
        self.assertEqual(type(state_dict['created_at']), str)
        self.assertEqual(type(state_dict['updated_at']), str)
        self.assertEqual(state_dict['name'], 'California')

    def test_to_dict_and_back(self):
        """
        Test if a State instance can be recreated from its to_dict representation
        """
        state = State()
        state_dict = state.to_dict()
        new_state = State(**state_dict)
        self.assertEqual(state.to_dict(), new_state.to_dict())

    def tearDown(self):
        """
        Clean up: Remove the JSON file created during tests
        """
        try:
            os.remove('State.json')
        except FileNotFoundError:
            pass


if __name__ == '__main__':
    unittest.main()
