""" tests/unit/utils_test.py """""
import unittest

from viiteri.utils.filter import lex_keywords, Token


class TestUtils(unittest.TestCase):
    """ Test class for utils """

    def setUp(self):
        self.query_string = "Maija,teppo,&Katja"

    def test_filter_lex_keywords(self):
        """ Test lex_keywords function """
        expected = [
            (Token.OR, "maija"),
            (Token.OR, "teppo"),
            (Token.AND, "katja")
        ]
        result = lex_keywords(self.query_string)
        self.assertEqual(result, expected)
