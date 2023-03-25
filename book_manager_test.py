import unittest
import json
from io import StringIO
from unittest.mock import patch

from book_manager import getAllIdList


class TestBook(unittest.TestCase):
    def setUp(self):
        # Create a books_test.json file with sample data
        with open('books_test.json', 'w') as file:
            json.dump({'books_details': [
                {'id': '1', 'title': 'Book 1', 'author': 'Author 1', 'publisher': 'Publisher 1', 'year': 2020},
                {'id': '2', 'title': 'Book 2', 'author': 'Author 2', 'publisher': 'Publisher 2', 'year': 2021},
                {'id': '3', 'title': 'Book 3', 'author': 'Author 3', 'publisher': 'Publisher 3', 'year': 2022}
            ]}, file)

    def test_getAllIdList(self):
        self.assertEqual(getAllIdList('books_test.json'), ['1', '2', '3'])

unittest.main()