import unittest
from app.core.parser.parser import Parser


class ParserTestCase(unittest.TestCase):

    parser = Parser("Bonjour GrandPy, tu connais la tour eiffel ?")
    expected = ["tour", "eiffel"]

    def test_clean_string(self):
        self.assertEqual(self.parser.clean_string(), self.expected)
