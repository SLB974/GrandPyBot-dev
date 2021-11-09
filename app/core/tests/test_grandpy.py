import unittest
from app.core.grandpy.grandpy import GrandPy
from app.core.grandpy.utils import grandpy_response, grandpy_none, grandpy_catch_phrase
from app.core.grandpy.utils import grandpy_catch_wiki, grandpy_error, grandpy_next


class GrandPyTestCase(unittest.TestCase):

    grandpy = GrandPy()

    def test_empty_response(self):
        self.assertIn(self.grandpy.empty_response(), grandpy_none)

    def test_catch_phrase(self):
        self.assertIn(self.grandpy.catch_phrase(), grandpy_catch_phrase)

    def test_error_response(self):
        self.assertIn(self.grandpy.error_response(), grandpy_error)

    def test_anecdote(self):
        self.assertIn(self.grandpy.anecdote(), grandpy_catch_wiki)

    def test_positive_response(self):
        self.assertIn(self.grandpy.positive_response(), grandpy_response)

    def test_next_query(self):
        self.assertIn(self.grandpy.next_query(), grandpy_next)
