""" tests/unit/reference_entity_test.py """

import unittest

from viiteri.entities.references import Article, Book, Inproceedings, inproceedings


class TestReferenceEntity(unittest.TestCase):
    """ Test class for Reference - entities """

    def setUp(self):
        self.test_article = Article(cite_key="petpet", author="Petteri",
                                    title="Petterin Kirja",
                                    journal="Petterin Kirjakokoelma", year="2003", volume="1")
        self.test_book = Book(cite_key="petkir", author="Petteri",
                              editor="Petteri", title="Petterin Kirja vol 2",
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
        self.assertEqual(self.test_book.editor, "Petteri")
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
            Article(cite_key="petpet", author="Petteri",
                    title="Petterin Kirja", journal="Petterin Kirjakokoelma")

    def test_init_book_with_missing_required_arguments(self):
        """ Test that Book-entity raises ValueError with invalid arguments """

        with self.assertRaises(ValueError):
            Book(cite_key="petkir", author="Petteri",
                 editor="Petteri", publisher="WSOY",
                 year="2004")

    def test_init_inproceedings_with_missing_required_arguments(self):
        """ Test that Inproceedings-entity raises ValueError with invalid arguments  """

        with self.assertRaises(ValueError):
            Inproceedings(cite_key="johinp", author="John Doe",
                          title="An Analysis of Example", booktitle="Sample Text",
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
                                       "'note': None, "
                                       "'issn': None, "
                                       "'zblnumber': None, "
                                       "'eprint': None}"))

    def test_book_str_method(self):
        """ Test that Book entitys str method returns correct string """
        book_str = str(self.test_book)
        self.assertEqual(book_str, ("{'_type': 'book', "
                                    "'_cite_key': 'petkir', "
                                    "'author': 'Petteri', "
                                    "'editor': 'Petteri', "
                                    "'title': 'Petterin Kirja vol 2', "
                                    "'publisher': 'WSOY', "
                                    "'year': '2004', "
                                    "'number': None, "
                                    "'volume': None, "
                                    "'pages': None, "
                                    "'month': None, "
                                    "'note': None, "
                                    "'doi': None, "
                                    "'issn': None, "
                                    "'isbn': None}"))

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

    # ieee format tests:

    def test_article_format_ieee(self):
        """Article entity is correctly converted to IEEE format"""
        article_ieee = 'Petteri, Petterin Kirja, Petterin Kirjakokoelma, 1, 2003'

        article_entity = Article(cite_key="petpet", author="Petteri Petterinpoika",
                                 title="Petterin Kirja",
                                 journal="Petterin Kirjakokoelma", year="2003", volume="1")
        another_article_ieee = 'P. Petterinpoika, Petterin Kirja, Petterin Kirjakokoelma, 1, 2003'

        self.assertEqual(article_ieee, self.test_article.format_ieee())
        self.assertEqual(another_article_ieee, article_entity.format_ieee())

    def test_book_format_ieee(self):
        """Book entity is correctly converted to IEEE format"""
        book_ieee = 'Petteri, Ed. Petterin Kirja vol 2, WSOY, 2004'

        book_entity = Book(cite_key="petkir", author="Petteri Petterinpoika", editor="Petteri",
                           title="Petterin Kirja vol 2", publisher="WSOY", year="2004")
        another_book_ieee = 'P. Petterinpoika, Petterin Kirja vol 2, Petteri, WSOY, 2004'

        self.assertEqual(book_ieee, self.test_book.format_ieee())
        self.assertEqual(another_book_ieee, book_entity.format_ieee())

    def test_inproceedings_format_ieee(self):
        """Inproceedings entity is correctly converted to IEEE format"""
        inproceedings_ieee = 'J. Doe, An Analysis of Example, Sample Text, Ex Ample, 2002'

        inp_entity = Inproceedings(cite_key="johinp", author="Doe",
                                   title="An Analysis of Example",
                                   booktitle="Sample Text",
                                   year="2002", editor="Ex Ample")
        inp_ieee_surname_only = 'Doe, An Analysis of Example, Sample Text, Ex Ample, 2002'

        self.assertEqual(inproceedings_ieee, self.test_inproceedings.format_ieee())
        self.assertEqual(inp_ieee_surname_only, inp_entity.format_ieee())

    def test_inproceedings_format_bibtex(self):
        """Inproceedings entity is correctly converted to BibTeX format"""
        inproceedings_bibtex = """@inproceedings{johinp,
        author = "John Doe",
        title = "An Analysis of Example",
        booktitle = "Sample Text",
        year = "2002",
        editor = "Ex Ample"
}"""

        print("First")
        print(inproceedings_bibtex)
        print("Second")
        print(self.test_inproceedings.format_bibtex())
        self.assertEqual(inproceedings_bibtex, self.test_inproceedings.format_bibtex())