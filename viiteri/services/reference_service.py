""" viiteri/services/reference_service """

from viiteri.repositories.reference_repository import reference_repository as default_repository
from viiteri.entities.references import Reference
from viiteri.utils.reference_factory import ReferenceFactory


class ReferenceService:
    """ Service for handling references """

    def __init__(self, reference_repository=default_repository):
        self._reference_repository = reference_repository

    def get_all_references(self) -> list[tuple[int, Reference]]:
        """ Returns all references """
        return self._reference_repository.get_all_references()
    
    def get_sorted_references(self, sort_type='author', reversed=False):
        references = self._reference_repository.get_all_references()
        if sort_type == 'author':
            print(type(references[2][1]))
            print(hasattr(references[2][1], 'author'))
            #print(references[0][1].author)
            references.sort(key=lambda x: x[1].author, reverse=reversed)
        elif sort_type == 'title':
            references.sort(key=lambda x: x[1].title, reverse=reversed)
        elif sort_type == 'year':
            references.sort(key=lambda x: x[1].year, reverse=not reversed)
        return references

    def create_reference(self, reference_type, **kwargs) -> int:
        """ Creates a new reference """
        new_reference = ReferenceFactory.create_reference(
            reference_type, **kwargs)
        return self._reference_repository.add_reference(new_reference)

    def remove_reference(self, ref_id: int):
        """ Removes a reference """
        return self._reference_repository.remove_reference(ref_id)


reference_service = ReferenceService()
