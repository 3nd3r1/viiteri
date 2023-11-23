""" tests/unit/reference_service_test.py """

import unittest

from viiteri.entities.reference import Reference
from viiteri.services.reference_service import ReferenceService


class ArticleRepositoryStub:
    """ Stub class for ArticleRepository """

    def __init__(self):
        self._references = [Reference(cite_key="petpet", author="Petteri",
                                      title="Petterin Kirja",
                                      journal="Petterin Kirjakokoelma", year="2003"),
                            Reference(cite_key="petpet2", author="Petteri",
                                      title="Petterin Kirja 2",
                                      journal="Petterin Kirjakokoelma", year="2005")]

    def get_all_references(self):
        """ Returns all references """
        return self._references

    def add_reference(self, reference):
        """ Stub method for add_article_reference """
        self._references.append(reference)
        return reference


class TestReferenceService(unittest.TestCase):
    """ Test class for ReferenceService """

    def setUp(self):
        self.reference_service = ReferenceService(ArticleRepositoryStub())

    def test_get_all_references(self):
        """ Test get_all_references """

        references = self.reference_service.get_all_references()

        self.assertEqual(len(references), 2)
        self.assertEqual(references[0].cite_key, "petpet")
        self.assertEqual(references[1].cite_key, "petpet2")

    def test_create_reference(self):
        """ Test that create_reference returns a valid bibtex string """
        result = self.reference_service.create_reference(cite_key="zimmerman2002becoming",
                                                         title=("Becoming a self-regulated learner:"
                                                                " An overview"),
                                                         author="Zimmerman, Barry J",
                                                         journal="Theory into practice",
                                                         year="2003",
                                                         volume="41")

        self.assertEqual(result.cite_key, "zimmerman2002becoming")
