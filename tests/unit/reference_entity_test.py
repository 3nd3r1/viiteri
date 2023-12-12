""" tests/unit/reference_entity_test.py """

import unittest

from viiteri.entities.references import Article, Book, Inproceedings

class TestReferenceEntity(unittest.TestCase):
    """ Test class for Reference - entities """

    def setUp(self):
        self.test_article = Article(cite_key="petpet", author="Petteri",
                                    title="Petterin Kirja",
                                    journal="Petterin Kirjakokoelma",
                                    year="2003", volume="1")
        self.test_book = Book(cite_key="petkir", author="Petteri",
                              title="Petterin Kirja vol 2",
                              publisher="WSOY", year="2004")
        self.test_inproceedings = Inproceedings(cite_key="johinp", author="John Doe",
                                                title="An Analysis of Example",
                                                booktitle="Sample Text",
                                                year="2002", editor="Ex Ample")

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

    def test_book_constructor(self):
        """ Test that Book-entity is correctly instantiated """
        # Test that abstract fields are set
        self.assertEqual(self.test_book.type, "book")
        self.assertEqual(self.test_book.cite_key, "petkir")

        # Test that required fields are set
        self.assertEqual(self.test_book.author, "Petteri")
        self.assertEqual(self.test_book.title, "Petterin Kirja vol 2")
        self.assertEqual(self.test_book.publisher, "WSOY")
        self.assertEqual(self.test_book.year, "2004")

    def test_inproceedings_constructor(self):
        """ Test that Inproceeding-entity is correctly instantiated """
        # Test that abstract fields are set
        self.assertEqual(self.test_inproceedings.type, "inproceedings")
        self.assertEqual(self.test_inproceedings.cite_key, "johinp")

        # Test that required fields are set
        self.assertEqual(self.test_inproceedings.author, "John Doe")
        self.assertEqual(self.test_inproceedings.title,
                         "An Analysis of Example")
        self.assertEqual(self.test_inproceedings.booktitle, "Sample Text")
        self.assertEqual(self.test_inproceedings.year, "2002")

        # Test that optional fields are set
        self.assertEqual(self.test_inproceedings.editor, "Ex Ample")

    def test_init_article_with_missing_required_arguments(self):
        """ Test that Article entity raises ValueError with invalid arguments """

        with self.assertRaises(ValueError):
            Article(cite_key="petpet",
                    author="Petteri",
                    title="Petterin Kirja",
                    journal="Petterin Kirjakokoelma")

    def test_init_book_with_missing_required_arguments(self):
        """ Test that Book-entity raises ValueError with invalid arguments """

        with self.assertRaises(ValueError):
            Book(cite_key="petkir",
                 author="Petteri",
                 publisher="WSOY",
                 year="2004")

    def test_init_inproceedings_with_missing_required_arguments(self):
        """ Test that Inproceedings-entity raises ValueError with invalid arguments  """

        with self.assertRaises(ValueError):
            Inproceedings(cite_key="johinp",
                          author="John Doe",
                          title="An Analysis of Example",
                          booktitle="Sample Text",
                          editor="Ex Ample")

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
                                       "'issn': None, "
                                       "'zblnumber': None, "
                                       "'eprint': None, "
                                       "'note': None, "
                                       "'annote': None}"))

    def test_book_str_method(self):
        """ Test that Book entitys str method returns correct string """
        book_str = str(self.test_book)
        self.assertEqual(book_str, ("{'_type': 'book', "
                                    "'_cite_key': 'petkir', "
                                    "'author': 'Petteri', "
                                    "'title': 'Petterin Kirja vol 2', "
                                    "'publisher': 'WSOY', "
                                    "'year': '2004', "
                                    "'editor': None, "
                                    "'edition': None, "
                                    "'volume': None, "
                                    "'number': None, "
                                    "'pages': None, "
                                    "'month': None, "
                                    "'series': None, "
                                    "'address': None, "
                                    "'doi': None, "
                                    "'issn': None, "
                                    "'isbn': None, "
                                    "'note': None, "
                                    "'annote': None}"))

    def test_inproceedings_str_method(self):
        """ Test that Inproceedings entitys str method returns correct string """
        inproceedings_str = str(self.test_inproceedings)
        self.assertEqual(inproceedings_str, ("{'_type': 'inproceedings', "
                                             "'_cite_key': 'johinp', "
                                             "'author': 'John Doe', "
                                             "'title': 'An Analysis of Example', "
                                             "'booktitle': 'Sample Text', "
                                             "'year': '2002', "
                                             "'editor': 'Ex Ample', "
                                             "'volume': None, "
                                             "'number': None, "
                                             "'series': None, "
                                             "'pages': None, "
                                             "'month': None, "
                                             "'address': None, "
                                             "'organization': None, "
                                             "'publisher': None, "
                                             "'note': None, "
                                             "'annote': None}"))
        
    def test_article_format_bibtex(self):
        """Article entity is correctly converted to BibTeX format"""
        article_bibtex = """@article{petpet,
        author = "Petteri",
        title = "Petterin Kirja",
        journal = "Petterin Kirjakokoelma",
        year = "2003",
        volume = "1"
}"""
        self.assertEqual(article_bibtex, self.test_article.format_bibtex())

    def test_book_format_bibtex(self):
        """Book entity is correctly converted to BibTeX format"""
        book_bibtex = """@book{petkir,
        author = "Petteri",
        title = "Petterin Kirja vol 2",
        publisher = "WSOY",
        year = "2004"
}"""

        self.assertEqual(book_bibtex, self.test_book.format_bibtex())

    def test_inproceedings_format_bibtex(self):
        """Inproceedings entity is correctly converted to BibTeX format"""
        inproceedings_bibtex = """@inproceedings{johinp,
        author = "John Doe",
        title = "An Analysis of Example",
        booktitle = "Sample Text",
        year = "2002",
        editor = "Ex Ample"
}"""

        self.assertEqual(inproceedings_bibtex, self.test_inproceedings.format_bibtex())
