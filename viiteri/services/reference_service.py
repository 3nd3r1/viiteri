from repositories.reference_repository import ReferenceRepository as default_reference_repository

class ReferenceService:
    def __init__(self, reference_repository=default_reference_repository):
        self._reference_repository = default_reference_repository

    def get_all_references(self):
        return self._reference_repository.get_all_references()
    
reference_service = ReferenceService()