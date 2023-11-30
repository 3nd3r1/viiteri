""" tests/unit/reference_service_test.py """

import unittest

from viiteri.entities.references import Article, Book, Inproceedings
from viiteri.services.reference_service import ReferenceService


class ReferenceRepositoryStub:
    """ Stub class for ReferenceRepository """

    def __init__(self):
        self._references = [Article(cite_key="petpet", author="Petteri",
                                    title="Petterin Kirja",
                                    journal="Petterin Kirjakokoelma", year="2003"),
                            Book(cite_key="petkir", author="Petteri", 
                                 editor="Petteri", title="Petterin Kirja vol 2", 
                                 publisher="WSOY", year="2004"),
                            Inproceedings(cite_key="johinp", author="John Doe",
                                         title="An Analysis of Example", booktitle="Sample Text",
                                         year="2002", editor="Ex Ample")]

    def get_all_references(self):
        """ Returns all references """
        return self._references

    def add_reference(self, reference):
        """ Stub method for add_reference """
        self._references.append(reference)
        return reference


class TestReferenceService(unittest.TestCase):
    """ Test class for ReferenceService """

    def setUp(self):
        self.reference_service = ReferenceService(ReferenceRepositoryStub())

    def test_get_all_references(self):
        """ Test get_all_references """

        references = self.reference_service.get_all_references()

        self.assertEqual(len(references), 3)
        self.assertEqual(references[0].cite_key, "petpet")
        self.assertEqual(references[1].cite_key, "petkir")
        self.assertEqual(references[2].cite_key, "johinp")

    def test_create_reference(self):
        """ Test that create_reference returns a valid bibtex string """
        result_article = self.reference_service.create_reference("article",
                                                         cite_key="zimmerman2002becoming",
                                                         title=("Becoming a self-regulated learner:"
                                                                " An overview"),
                                                         author="Zimmerman, Barry J",
                                                         journal="Theory into practice",
                                                         year="2003",
                                                         volume="41")
        result_book = self.reference_service.create_reference("book",
                                                              cite_key="CI",
                                                              author="Duvall, Paul",
                                                              title="Continuous Integration: Improving Software Quality and Reducing Risk",
                                                              year="2007",
                                                              publisher="Addison-Wesley",
                                                              editor="editor")
        result_inproceedings = self.reference_service.create_reference("inproceedings",
                                                                      cite_key="johinp",
                                                                      author="John Doe",
                                                                      title="An Analysis of Example",
                                                                      booktitle="Sample Text",
                                                                      year="2002",
                                                                      editor="Ex Ample")

        self.assertEqual(result_article.cite_key, "zimmerman2002becoming")
        self.assertEqual(result_book.cite_key, "CI")
        self.assertEqual(result_inproceedings.cite_key, "johinp")