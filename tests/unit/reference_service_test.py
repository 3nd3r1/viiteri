""" tests/unit/reference_service_test.py """

import unittest
from viiteri.services.reference_service import ReferenceService

class ArticleRepositoryStub:
    """ Stub class for ArticleRepository """

    def get_all_references(self):
        """ Returns all references """
        return ["reference1", "reference2"]

class TestReferenceService(unittest.TestCase):
    """ Test class for ReferenceService """

    def setUp(self):
        self.reference_service = ReferenceService(ArticleRepositoryStub())

    def test_get_all_references(self):
        """ Test get_all_references """

        references = self.reference_service.get_all_references()

        self.assertEqual(len(references), 2)
        self.assertEqual(references[0], "reference1")
        self.assertEqual(references[1], "reference2")
