""" tests/unit/reference_service_test.py """

import unittest

from unittest.mock import patch, MagicMock
from requests.exceptions import Timeout

from viiteri.entities.references import Article, Book, Inproceedings
from viiteri.services.reference_service import ReferenceService


class ReferenceRepositoryStub:
    """ Stub class for ReferenceRepository """

    def __init__(self):
        self._references = [(1, Article(cite_key="petpet", author="Petteri",
                                    title="Petterin Kirja",
                                    journal="Petterin Kirjakokoelma", year="2003")),
                            (2, Book(cite_key="petkir", author="Petteri",
                                 editor="Petteri", title="Petterin Kirja vol 2",
                                 publisher="WSOY", year="2004")),
                            (3, Inproceedings(cite_key="johinp", author="John Doe",
                                          title="An Analysis of Example", booktitle="Sample Text",
                                          year="2002", editor="Ex Ample"))]
        self._id = len(self._references)

    def _assign_id(self):
        """ Assigns an id to a reference """
        self._id += 1
        return self._id

    def get_all_references(self):
        """ Returns all references """
        return self._references

    def add_reference(self, reference):
        """ Stub method for add_reference """
        ref = (self._assign_id(), reference)
        self._references.append(ref)
        return ref
    
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
        self.assertEqual(references[0][1].cite_key, "petpet")
        self.assertEqual(references[1][1].cite_key, "petkir")
        self.assertEqual(references[2][1].cite_key, "johinp")

    def test_create_reference(self):
        """ Test that create_reference adds a new reference """
        references = self.reference_service.get_all_references()
        self.assertEqual(len(references), 3)
        self.reference_service.create_reference("article", cite_key="petpet", author="Petteri",
                                                title="Petterin Kirja",
                                                journal="Petterin Kirjakokoelma", year="2003")
        references = self.reference_service.get_all_references()
        self.assertEqual(len(references), 4)
        self.assertEqual(type(references[3][1]), Article)
        self.assertEqual(references[3][1].cite_key, "petpet")
        self.reference_service.create_reference("book", cite_key="petkir", author="Petteri",
                                                editor="Petteri", title="Petterin Kirja vol 2",
                                                publisher="WSOY", year="2004")
        references = self.reference_service.get_all_references()
        self.assertEqual(len(references), 5)
        self.assertEqual(type(references[4][1]), Book)
        self.assertEqual(references[4][1].cite_key, "petkir")
        self.reference_service.create_reference("inproceedings", cite_key="johinp", author="John Doe",
                                                title="An Analysis of Example", booktitle="Sample Text",
                                                year="2002", editor="Ex Ample")
        references = self.reference_service.get_all_references()
        self.assertEqual(len(references), 6)
        self.assertEqual(type(references[5][1]), Inproceedings)
        self.assertEqual(references[5][1].cite_key, "johinp")

    def test_remove_reference(self):
        """ Test that remove_reference removes the correct reference """
        self.reference_service.remove_reference(0)
        references = self.reference_service.get_all_references()
        self.assertEqual(len(references), 2)
        self.assertEqual(references[0][1].cite_key, "petkir")
        self.assertEqual(references[1][1].cite_key, "johinp")
        self.reference_service.remove_reference(0)
        references = self.reference_service.get_all_references()
        self.assertEqual(len(references), 1)
        self.assertEqual(references[0][1].cite_key, "johinp")
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
        
        test_query = "kirsi,timo,&2000" #kirsi tai timo, ja 2000
        references = self.reference_service.get_filtered_references(test_query)
        self.assertEqual(len(references), 2)
        self.assertEqual(references[0][1].cite_key, "kirart")
        self.assertEqual(references[1][1].cite_key, "timart")

        test_query = "kirsi" #kirsi
        references = self.reference_service.get_filtered_references(test_query)
        self.assertEqual(len(references), 2)
        self.assertEqual(references[0][1].cite_key, "kirart")
        self.assertEqual(references[1][1].cite_key, "kirboo")

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

    @patch('viiteri.services.reference_service.get')
    def test_get_reference_by_doi_failed_to_find_reference(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        with self.assertRaises(ValueError) as context:
            self.reference_service.get_reference_by_doi("https://dl.acm.org/doi/10.1145/2380552.2380613")

        self.assertEqual(str(context.exception), "Failed to find reference")

    @patch('viiteri.services.reference_service.get')
    def test_get_reference_by_doi_timeout(self, mock_get):
        mock_get.side_effect = Timeout

        with self.assertRaises(TimeoutError) as context:
            self.reference_service.get_reference_by_doi("https://dl.acm.org/doi/10.1145/2380552.2380613")

        self.assertEqual(str(context.exception), "Request timed out")

    def test_sort_by_author(self):
        """ Test get_sorted_references with sort_type author """

        references = self.reference_service.get_sorted_references('author')

        self.assertEqual(references[0][1].cite_key, "johinp")
        self.assertEqual(references[1][1].cite_key, "petpet")
        self.assertEqual(references[2][1].cite_key, "petkir")
    
    def test_sort_by_title(self):
        """ Test get_sorted_references with sort_type title """

        references = self.reference_service.get_sorted_references('title')

        self.assertEqual(references[0][1].cite_key, "johinp")
        self.assertEqual(references[1][1].cite_key, "petpet")
        self.assertEqual(references[2][1].cite_key, "petkir")
    
    def test_sort_by_year(self):
        """ Test get_sorted_references with sort_type year """

        references = self.reference_service.get_sorted_references('year')

        self.assertEqual(references[0][1].cite_key, "johinp")
        self.assertEqual(references[1][1].cite_key, "petpet")
        self.assertEqual(references[2][1].cite_key, "petkir")
    
    def test_sort_ascending_order(self):
        """ Test get_sorted_references in ascending order """

        references = self.reference_service.get_sorted_references('year', 'asc')

        self.assertEqual(references[0][1].cite_key, "petkir")
        self.assertEqual(references[1][1].cite_key, "petpet")
        self.assertEqual(references[2][1].cite_key, "johinp")
