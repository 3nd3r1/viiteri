""" viiteri/services/reference_service """
from viiteri.repositories.article_repository import ArticleRepository as default_repository

class ReferenceService:
    """ Service for handling references """
    def __init__(self, reference_repository=default_repository):
        self._reference_repository = reference_repository

    def get_all_references(self):
        """ Returns all references """
        return self._reference_repository.get_all_references()

reference_service = ReferenceService()
