""" tests/unit/reference_service_test.py """

import unittest
from pybtex.database import BibliographyData, Entry
from viiteri.services.reference_service import ReferenceService

class ArticleRepositoryStub:
    """ Stub class for ArticleRepository """

    def add_reference(self, _bib_data):
        """ Stub method for add_article_reference """
        cite_key = 'zimmerman2002becoming'
        cite_type = 'article'
        fields = [('title', 'Becoming a self-regulated learner: An overview'),
                  ('author', 'Zimmerman, Barry J'),
                  ('journal', 'Theory into practice'),
                  ('volume', '41'),
                  ('number', '2'),
                  ('pages', '64--70'),
                  ('year', '2002'),
                  ('publisher', 'Taylor & Francis')]
        return BibliographyData({cite_key: Entry(cite_type, fields)}).to_string('bibtex')

class TestReferenceService(unittest.TestCase):
    """ Test class for ReferenceService """
    def setUp(self):
        self.reference_service = ReferenceService(ArticleRepositoryStub())

    def test_create_reference(self):
        """ Test that create_reference returns a valid bibtex string """

        cite_key = 'zimmerman2002becoming'
        cite_type = 'article'
        fields = [('title', 'Becoming a self-regulated learner: An overview'),
                  ('author', 'Zimmerman, Barry J'),
                  ('journal', 'Theory into practice'),
                  ('volume', '41'),
                  ('number', '2'),
                  ('pages', '64--70'),
                  ('year', '2002'),
                  ('publisher', 'Taylor & Francis')]
        bib_data = BibliographyData({cite_key: Entry(cite_type, fields)})

        result = self.reference_service.create_reference(cite_key, fields, cite_type)

        self.assertEqual(bib_data.to_string('bibtex'), result)
