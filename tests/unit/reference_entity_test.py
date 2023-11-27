""" tests/unit/reference_entity_test.py """

import unittest

from viiteri.entities.reference import Article


class TestReferenceEntity(unittest.TestCase):
    """ Test class for Reference - entities """

    def setUp(self):
        self.test_article = Article(cite_key="petpet", author="Petteri",
                                    title="Petterin Kirja",
                                    journal="Petterin Kirjakokoelma", year="2003", volume="1")

    def test_article_constructor(self):
        """ Test that Article entity is correctly instantiated """
        # Test that abstract fields are set
        self.assertEqual(self.test_article.type, "article")
        self.assertEqual(self.test_article.cite_key, "petpet")

        # Test that required fields are set
        self.assertEqual(self.test_article.author, "Petteri")
        self.assertEqual(self.test_article.title, "Petterin Kirja")
        self.assertEqual(self.test_article.journal, "Petterin Kirjakokoelma")
        self.assertEqual(self.test_article.year, "2003")

        # Test that optional fields are set
        self.assertEqual(self.test_article.volume, "1")

    def test_init_article_with_missing_required_arguments(self):
        """ Test that Article entity raises ValueError with invalid arguments """

        with self.assertRaises(ValueError):
            Article(cite_key="petpet", author="Petteri",
                    title="Petterin Kirja", journal="Petterin Kirjakokoelma")

    def test_article_str_method(self):
        """ Test that Article entitys str method returns correct string """
        article_str = str(self.test_article)
        self.assertEqual(article_str, ("{'_type': 'article', "
                                       "'_cite_key': 'petpet', "
                                       "'author': 'Petteri', "
                                       "'title': 'Petterin Kirja', "
                                       "'journal': 'Petterin Kirjakokoelma', "
                                       "'year': '2003', "
                                       "'volume': '1', "
                                       "'number': None, "
                                       "'pages': None, "
                                       "'month': None, "
                                       "'doi': None, "
                                       "'note': None, "
                                       "'issn': None, "
                                       "'zblnumber': None, "
                                       "'eprint': None}"))
