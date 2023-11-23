""" tests/unit/reference_repository_test.py """

import unittest

from viiteri.entities.reference import Reference
from viiteri.repositories.reference_repository import reference_repository


class TestReferenceRepository(unittest.TestCase):
    """ Class for unit testing reference_repository """

    def setUp(self):
        reference_repository.delete_all()
        self.test_reference = Reference(cite_key="petpet", author="Petteri",
                                        title="Petterin Kirja",
                                        journal="Petterin Kirjakokoelma", year="2003")

    def test_add_reference(self):
        """ Test adding a reference to the repository """
        reference_repository.add_reference(self.test_reference)
        references = reference_repository.get_all_references()

        self.assertEqual(len(references), 1)
        self.assertEqual(references[0].cite_key, "petpet")

    def test_delete_all_references(self):
        """ Test deleting all references from the repository """
        reference_repository.add_reference(self.test_reference)
        reference_repository.delete_all()

        self.assertEqual(len(reference_repository.get_all_references()), 0)
