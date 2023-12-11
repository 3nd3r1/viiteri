import unittest

from viiteri.utils.filter import lex_keywords, Token

class TestFilter(unittest.TestCase):
    """ Test class for filter functions """
    def setUp(self):
        self.query_string = "Maija,teppo,&Katja"
    def test_lex_keywords(self):
        expected = [
            (Token.OR, "maija"),
            (Token.OR, "teppo"),
            (Token.AND, "katja")
        ]
        result = lex_keywords(self.query_string)
        self.assertEqual(result, expected)
