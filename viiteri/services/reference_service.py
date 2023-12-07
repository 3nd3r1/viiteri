""" viiteri/services/reference_service """

from subprocess import run, PIPE
from bibtexparser import loads
from viiteri.repositories.reference_repository import reference_repository as default_repository
from viiteri.entities.references import Reference
from viiteri.utils.reference_factory import ReferenceFactory


class ReferenceService:
    """ Service for handling references """

    def __init__(self, reference_repository=default_repository):
        self._reference_repository = reference_repository

    def get_all_references(self) -> list[(int, Reference)]:
        """ Returns all references """
        return self._reference_repository.get_all_references()

    def create_reference(self, reference_type, **kwargs) -> int:
        """ Creates a new reference """
        new_reference = ReferenceFactory.create_reference(
            reference_type, **kwargs)
        return self._reference_repository.add_reference(new_reference)

    def remove_reference(self, ref_id: int):
        """ Removes a reference """
        return self._reference_repository.remove_reference(ref_id)

    def get_reference_by_doi(self, doi: str):
        """ Returns a reference dictionary, takes a doi as input """
        command = "doi2bib " + doi
        bib_string = run(command, shell=True, stdout=PIPE, check=False).stdout.decode('utf-8')
        bib_dict = loads(bib_string).entries_dict
        cite_key = next(iter(bib_dict))
        data_dict = bib_dict[cite_key]
        return data_dict


reference_service = ReferenceService()
