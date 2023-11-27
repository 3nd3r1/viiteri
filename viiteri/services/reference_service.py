""" viiteri/services/reference_service """

from viiteri.repositories.reference_repository import reference_repository as default_repository
from viiteri.entities.reference import Reference
from viiteri.utils.reference_factory import ReferenceFactory


class ReferenceService:
    """ Service for handling references """

    def __init__(self, reference_repository=default_repository):
        self._reference_repository = reference_repository

    def get_all_references(self) -> list[Reference]:
        """ Returns all references """
        return self._reference_repository.get_all_references()

    def create_reference(self, reference_type, **kwargs):
        """ Creates a new reference """
        new_reference = ReferenceFactory.create_reference(
            reference_type, **kwargs)
        return self._reference_repository.add_reference(new_reference)


reference_service = ReferenceService()