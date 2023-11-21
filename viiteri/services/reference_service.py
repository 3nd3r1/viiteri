""" viiteri/services/reference_service """
from repositories.reference_repository import ReferenceRepository as default_reference_repository
from pybtex.database import BibliographyData, Entry

class ReferenceService:
    def __init__(self, reference_repository=default_reference_repository):
        self._reference_repository = reference_repository

    def get_all_references(self):
        return self._reference_repository.get_all_references()

    def create_reference(self, cite_key, fields, cite_type='article'):
        bib_data = BibliographyData({cite_key: Entry(cite_type, fields)})
        return self._reference_repository.create_reference(bib_data.to_string('bibtex'))
    
reference_service = ReferenceService()
