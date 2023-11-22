""" viiteri/repositories/reference_repository.py """
# from entities.article import Article
from sqlalchemy.sql import text
from viiteri.utils.db import get_database_connection



class ReferenceRepository:
    """Handles the reference database."""
    def __init__(self, connection):
        self._connection = connection

    def add_reference(self, content):
        """Adds a new reference to the database."""
        cursor = self._connection.session()
        cursor.execute(text(
            'insert into reference_table (content) values (:content);'),
            {"content":content}
        )
        cursor.commit()

    def get_all_references(self):
        """Gets all references from the database"""
        cursor = self._connection.session()
        result = cursor.execute(text(
            'select content from reference_table;'
        ))
        references = result.fetchall()
        return references
    
    def delete_all(self):
        """Empties whole database"""
        cursor = self._connection.session()
        cursor.execute(text('delete from reference_table'))
        cursor.commit()


reference_repository = ReferenceRepository(get_database_connection())
