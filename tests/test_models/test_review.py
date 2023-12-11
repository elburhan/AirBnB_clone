import unittest
from models.review import Review
from datetime import datetime
import os
import json


class TestReview(unittest.TestCase):
    """
    Test the Review class
    """
    def test_init(self):
        """
        Test the initialization of the Review
        """
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertTrue(hasattr(review, 'id'))
        self.assertTrue(hasattr(review, 'created_at'))
        self.assertTrue(hasattr(review, 'updated_at'))
        self.assertEqual(type(review.id), str)
        self.assertEqual(type(review.created_at), datetime)
        self.assertEqual(type(review.updated_at), datetime)
        self.assertEqual(review.place_id, '')
        self.assertEqual(review.user_id, '')
        self.assertEqual(review.text, '')

    def test_str(self):
        """
        Test the __str__ method of the Review
        """
        review = Review()
        string_representation = str(review)
        self.assertIn('[Review]', string_representation)
        self.assertIn('id', string_representation)
        self.assertIn('created_at', string_representation)
        self.assertIn('updated_at', string_representation)

    def test_save(self):
        """
        Test the save method of the Review
        """
        review = Review()
        original_updated_at = review.updated_at
        review.save()
        self.assertNotEqual(original_updated_at, review.updated_at)

    def test_to_dict(self):
        """
        Test the to_dict method of the Review
        """
        review = Review()
        review_dict = review.to_dict()
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertEqual(type(review_dict['created_at']), str)
        self.assertEqual(type(review_dict['updated_at']), str)
        self.assertEqual(review_dict['place_id'], '')
        self.assertEqual(review_dict['user_id'], '')
        self.assertEqual(review_dict['text'], '')

    def test_to_dict_with_args(self):
        """
        Test the to_dict method of the Review with additional arguments
        """
        review = Review(
            id='123',
            created_at=datetime.now(),
            updated_at=datetime.now(),
            place_id='456',
            user_id='789',
            text='Great place, highly recommended!'
        )
        review_dict = review.to_dict()
        self.assertEqual(review_dict['id'], '123')
        self.assertEqual(type(review_dict['created_at']), str)
        self.assertEqual(type(review_dict['updated_at']), str)
        self.assertEqual(review_dict['place_id'], '456')
        self.assertEqual(review_dict['user_id'], '789')
        self.assertEqual(review_dict['text'], 'Great place, highly recommended!')

    def test_to_dict_and_back(self):
        """
        Test if a Review instance can be recreated from its to_dict representation
        """
        review = Review()
        review_dict = review.to_dict()
        new_review = Review(**review_dict)
        self.assertEqual(review.to_dict(), new_review.to_dict())

    def tearDown(self):
        """
        Clean up: Remove the JSON file created during tests
        """
        try:
            os.remove('Review.json')
        except FileNotFoundError:
            pass


if __name__ == '__main__':
    unittest.main()
