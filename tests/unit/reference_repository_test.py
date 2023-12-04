""" tests/unit/reference_repository_test.py """

import unittest

from viiteri.app import create_app
from viiteri.entities.references import Article, Book, Inproceedings
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
        self.test_inproceedings = Inproceedings(cite_key="johinp", author="John Doe",
                                                title="An Analysis of Example", booktitle="Sample Text",
                                                year="2002", editor="Ex Ample")

    def test_add_reference(self):
        """ Test adding all reference types to the repository """
        reference_repository.add_reference(self.test_article)
        reference_repository.add_reference(self.test_book)
        reference_repository.add_reference(self.test_inproceedings)
        references = reference_repository.get_all_references()

        self.assertEqual(len(references), 3)

        # testataan, että viitteiden id:t ovat 1, 2 ja 3
        self.assertEqual(references[0][0], 1)
        self.assertEqual(references[1][0], 2)
        self.assertEqual(references[2][0], 3)
        
        # testataan, että viitteen sisältö on oikea
        self.assertEqual(references[0][1].cite_key, "petpet")
        self.assertEqual(references[1][1].cite_key, "petkir")
        self.assertEqual(references[2][1].cite_key, "johinp")

    def test_delete_all_references(self):
        """ Test deleting all references from the repository """
        reference_repository.add_reference(self.test_article)
        reference_repository.add_reference(self.test_book)
        reference_repository.add_reference(self.test_inproceedings)
        reference_repository.delete_all()
        self.assertEqual(len(reference_repository.get_all_references()), 0)
