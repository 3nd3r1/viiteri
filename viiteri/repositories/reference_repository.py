""" viiteri/repositories/reference_repository.py """
# from entities.reference import Reference
from viiteri.utils.db import get_database_connection


class ReferenceRepository:
    """Handles the reference database."""
    def __init__(self, connection):
        self._connection = connection

    # lisää tietokantaan lähdeviitteen, parametrina reference olio
    def add_reference(self, reference):
        """Adds a new reference to the database."""
        cursor = self._connection.session()
        cursor.execute(
            'insert into reference_table (content) values (?);',
            (reference) # vai reference.content ?
        )
        self._connection.commit()

    def get_all_references(self):
        """Gets all references from the database and returns them as a list."""
        cursor = self._connection.session()
        cursor.execute(
            'select * from reference_table;'
        )
        references = cursor.fetchall()
        return list(references)


reference_repository = ReferenceRepository(get_database_connection())
