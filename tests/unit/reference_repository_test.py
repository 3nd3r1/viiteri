import unittest
from viiteri.repositories.reference_repository import reference_repository
# from viiteri.entities.article import Article

# class FakeReference:
#     def __init__(self, content):
#         self.content = content
    
# class FakeReferenceRepository:
#     def __init__(self, references=None):
#         self.references = references or []

#     def add_reference


class TestReferenceRepository(unittest.TestCase):
    def setUp(self):
        reference_repository.delete_all()
        
        self.reference = "Adam Zeve, 'Explained: Generative AI', MIT News, 2023"

    def test_add_reference(self):
        reference_repository.add_reference(self.reference)

        references = reference_repository.get_all_references()

        self.assertEqual(len(references), 1)
        self.assertEqual(references[0][0], self.reference)
    
    def test_delete_all_references(self):
        reference_repository.add_reference(self.reference)
        reference_repository.delete_all()

        self.assertEqual(len(reference_repository.get_all_references()), 0)
