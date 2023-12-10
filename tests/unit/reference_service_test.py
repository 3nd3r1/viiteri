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

    def test_get_reference_by_doi(self):
        """ Test that get_reference_by_doi works with a valid DOI and supported reference-type """
        reference_example_1 = self.reference_service.get_reference_by_doi("https://dl.acm.org/doi/10.1145/2380552.2380613")
        reference_example_2 = self.reference_service.get_reference_by_doi("10.1146/annurev-statistics-031017-100307")
        self.assertEqual(reference_example_1['year'], "2012")
        self.assertEqual(reference_example_1['month'], "October")
        self.assertEqual(reference_example_2['author'], "Held, Leonhard and Ott, Manuela")
        self.assertEqual(reference_example_2['issn'], "2326-831X")
    
    def test_get_reference_by_doi_raises_error_with_invalid_doi(self):
        """ Test that get_reference_by_doi raises error with invalid DOI """
        with self.assertRaises(ValueError) as error:
            self.reference_service.get_reference_by_doi("https://doi.org/3.1415926535")
        self.assertEqual(str(error.exception), "Invalid DOI")
        with self.assertRaises(ValueError) as error:
            self.reference_service.get_reference_by_doi("10.114/annurev-statistics-031017-100307")
        self.assertEqual(str(error.exception), "Invalid DOI")

    def test_get_reference_by_doi_raises_error_with_unsupported_reference_type(self):
        """ Test that get_reference_by_doi raises error with valid DOI and unsupported reference type """
        with self.assertRaises(ValueError) as error:
            self.reference_service.get_reference_by_doi("10.17077/etd.g638o927")
        self.assertEqual(str(error.exception), "Unsupported reference type phdthesis")
        with self.assertRaises(ValueError) as error:
            self.reference_service.get_reference_by_doi("https://doi.org/10.1007/0-387-21645-6_7")
        self.assertEqual(str(error.exception), "Unsupported reference type inbook")

