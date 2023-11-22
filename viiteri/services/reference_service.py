# pylint: disable=import-error, no-name-in-module

""" viiteri/services/reference_service """
from pybtex.database import BibliographyData, Entry
#from viiteri.repositories.article_repository import ArticleRepository as default_repository


class ReferenceService:
    """ Service for handling references """
    def __init__(self, reference_repository=None): #=default_repository
        self._reference_repository = reference_repository

    def create_reference(self, cite_key, fields, cite_type='article'):
        """ Creates a new reference """
        bib_data = BibliographyData({cite_key: Entry(cite_type, fields)})
        return self._reference_repository.add_article_reference(bib_data.to_string('bibtex'))

reference_service = ReferenceService()
