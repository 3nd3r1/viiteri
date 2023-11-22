from viiteri.utils.db import get_database_connection


class ReferenceRepository:
    def __init__(self, connection):
        self._connection = connection
    
    # lisää tietokantaan lähdeviitteen, parametrina reference olio
    def add_reference(self, reference):
        cursor = self._connection.cursor()
        cursor.execute(
            'insert into references (content) values (?);',
            (reference) # vai reference.content ?
        )
        self._connection.commit()
    
    def get_all_references(self):
        cursor = self._connection.cursor()
        cursor.execute(
            'select * from references;'
        )
        self._connection.commit()


reference_repository = ReferenceRepository(get_database_connection())