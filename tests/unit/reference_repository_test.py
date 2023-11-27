""" tests/unit/reference_repository_test.py """

import unittest

from viiteri.app import create_app
from viiteri.entities.references import Article, Book
from viiteri.repositories.reference_repository import reference_repository


class TestReferenceRepository(unittest.TestCase):
    """ Class for unit testing reference_repository """

    def setUp(self):
        self.app = create_app()
        self.app.app_context().push()

        reference_repository.delete_all()
        self.test_article = Article(cite_key="petpet", author="Petteri",
                                      title="Petterin Kirja",
                                      journal="Petterin Kirjakokoelma", year="2003")
        self.test_book = Book(cite_key="petkir", author="Petteri",
                              editor="Petteri", title="Petterin Kirja vol 2",
                              publisher="WSOY", year="2004")

    def test_add_reference(self):
        """ Test adding all reference types to the repository """
        reference_repository.add_reference(self.test_article)
        reference_repository.add_reference(self.test_book)
        references = reference_repository.get_all_references()

        self.assertEqual(len(references), 2)
        self.assertEqual(references[0].cite_key, "petpet")
        self.assertEqual(references[1].cite_key, "petkir")

    def test_delete_all_references(self):
        """ Test deleting all references from the repository """
        reference_repository.add_reference(self.test_article)
        reference_repository.add_reference(self.test_book)
        reference_repository.delete_all()
        self.assertEqual(len(reference_repository.get_all_references()), 0)
