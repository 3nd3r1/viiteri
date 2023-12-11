""" viiteri/services/reference_service """

from doi import find_doi_in_text, validate_doi
from requests import get
from requests.exceptions import Timeout
from bibtexparser import loads

from viiteri.repositories.reference_repository import reference_repository as default_repository
from viiteri.entities.references import Reference
from viiteri.utils.reference_factory import ReferenceFactory
from viiteri.utils.filter import keyword_filter_references


class ReferenceService:
    """ Service for handling references """

    def __init__(self, reference_repository=default_repository):
        self._reference_repository = reference_repository

    def get_all_references(self) -> list[tuple[int, Reference]]:
        """ Returns all references """
        return self._reference_repository.get_all_references()

    def get_filtered_references(self, keywords: str) -> list[tuple[int, Reference]]:
        """ Returns references based on keyword search"""
        return keyword_filter_references(
            keywords, self._reference_repository.get_all_references())

    def create_reference(self, reference_type, **kwargs) -> int:
        """ Creates a new reference """
        new_reference = ReferenceFactory.create_reference(
            reference_type, **kwargs)
        return self._reference_repository.add_reference(new_reference)

    def remove_reference(self, ref_id: int):
        """ Removes a reference """
        return self._reference_repository.remove_reference(ref_id)

    def get_reference_by_doi(self, doi: str):
        """ Returns a reference dictionary, takes a DOI as input """
        searched_doi = find_doi_in_text(doi)
        if searched_doi:
            doi = searched_doi
        try:
            validate_doi(doi)
        except ValueError as exc:
            raise ValueError("Invalid DOI") from exc

        url = f"https://dx.doi.org/{doi}"
        headers = {"Accept": "application/x-bibtex"}
        try:
            response = get(url, headers=headers, timeout=10)
        except Timeout as exc:
            raise TimeoutError("Request timed out") from exc

        if response.status_code == 200:
            bib_string = response.content.decode('utf-8')
            bib_dict = loads(bib_string).entries_dict
            cite_key = next(iter(bib_dict))
            data_dict = bib_dict[cite_key]
            if data_dict['ENTRYTYPE'] not in ['article', 'book', 'inproceedings']:
                raise ValueError(f"Unsupported reference type {data_dict['ENTRYTYPE']}")
            return data_dict
        raise ValueError("Failed to find reference")


reference_service = ReferenceService()
