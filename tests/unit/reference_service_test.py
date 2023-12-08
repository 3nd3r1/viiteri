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
    
    def remove_reference(self, ref_id):
        """ Stub method for remove_reference """
        self._references.pop(ref_id)


class TestReferenceService(unittest.TestCase):
    """ Test class for ReferenceService """

    def setUp(self):
        self.reference_service = ReferenceService(ReferenceRepositoryStub())

    def test_get_all_references(self):
        """ Test get_all_references """

        references = self.reference_service.get_all_references()

        self.assertEqual(len(references), 3)
        self.assertEqual(len(references), 3)
        self.assertEqual(references[0].cite_key, "petpet")
        self.assertEqual(references[1].cite_key, "petkir")
        self.assertEqual(references[2].cite_key, "johinp")
        self.assertEqual(references[2].cite_key, "johinp")

    def test_create_reference(self):
        """ Test that create_reference adds a new reference """
        references = self.reference_service.get_all_references()
        self.assertEqual(len(references), 3)
        self.reference_service.create_reference("article", cite_key="petpet", author="Petteri",
                                                title="Petterin Kirja",
                                                journal="Petterin Kirjakokoelma", year="2003")
        references = self.reference_service.get_all_references()
        self.assertEqual(len(references), 4)
        self.assertEqual(type(references[3]), Article)
        self.assertEqual(references[3].cite_key, "petpet")
        self.reference_service.create_reference("book", cite_key="petkir", author="Petteri",
                                                editor="Petteri", title="Petterin Kirja vol 2",
                                                publisher="WSOY", year="2004")
        references = self.reference_service.get_all_references()
        self.assertEqual(len(references), 5)
        self.assertEqual(type(references[4]), Book)
        self.assertEqual(references[4].cite_key, "petkir")
        self.reference_service.create_reference("inproceedings", cite_key="johinp", author="John Doe",
                                                title="An Analysis of Example", booktitle="Sample Text",
                                                year="2002", editor="Ex Ample")
        references = self.reference_service.get_all_references()
        self.assertEqual(len(references), 6)
        self.assertEqual(type(references[5]), Inproceedings)
        self.assertEqual(references[5].cite_key, "johinp")

    def test_remove_reference(self):
        """ Test that remove_reference removes the correct reference """
        self.reference_service.remove_reference(0)
        references = self.reference_service.get_all_references()
        self.assertEqual(len(references), 2)
        self.assertEqual(references[0].cite_key, "petkir")
        self.assertEqual(references[1].cite_key, "johinp")
        self.reference_service.remove_reference(0)
        references = self.reference_service.get_all_references()
        self.assertEqual(len(references), 1)
        self.assertEqual(references[0].cite_key, "johinp")
        self.reference_service.remove_reference(0)
        references = self.reference_service.get_all_references()
        self.assertEqual(len(references), 0)

    def test_get_filtered_references(self):
        self.reference_service.create_reference("article", cite_key="kirart", author="Kirsi",
                                                title="Testikirja",
                                                journal="Testikokoelma", year="2000")
        self.reference_service.create_reference("article", cite_key="timart", author="Timo",
                                                title="Testikirja 2",
                                                journal="Testikokoelma", year="2000")
        self.reference_service.create_reference("book", cite_key="kirboo", author="Kirsi",
                                                editor="Kirsi", title="Kirsin kirja",
                                                publisher="WSOY", year="2002")
        self.reference_service.create_reference("book", cite_key="timboo", author="Timo",
                                                editor="Timo", title="Timon kirja",
                                                publisher="WSOY", year="2002")
        
        test_query = "kirsi timo&2000" #kirsi tai timo, ja 2000
        references = self.reference_service.get_filtered_references(test_query)
        self.assertEqual(len(references), 2)
        self.assertEqual(references[0].cite_key, "kirart")
        self.assertEqual(references[1].cite_key, "timart")