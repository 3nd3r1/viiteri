from repositories.reference_repository import ReferenceRepository as default_reference_repository

class ReferenceService:
    def __init__(self, reference_repository=default_reference_repository):
        self._reference_repository = reference_repository

    def get_all_references(self):
        return self._reference_repository.get_all_references()
    
    def create_reference(self, author, title, journal, year, volume):
        return self._reference_repository.create_reference(author, title, journal, year, volume)
    
reference_service = ReferenceService()