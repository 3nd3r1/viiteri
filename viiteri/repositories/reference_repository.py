""" viiteri/repositories/reference_repository.py """
from sqlalchemy.sql import text

from viiteri.entities.reference import Reference
from viiteri.utils.db import db


class ReferenceRepository:
    """Handles the reference database."""

    def __init__(self, connection):
        self._connection = connection

    def add_reference(self, reference: Reference):
        """Adds a new reference to the database."""
        cursor = self._connection.session()
        cursor.execute(text(
            'insert into reference_table (content) values (:content);'),
            {"content": str(reference)}
        )
        cursor.commit()
        return reference

    def get_all_references(self) -> list[Reference]:
        """Gets all references from the database"""
        cursor = self._connection.session()
        result = cursor.execute(text(
            'select content from reference_table;'
        ))
        references = [Reference.from_str(content[0]) for content in result.fetchall()]
        return references

    def delete_all(self):
        """Empties whole database"""
        cursor = self._connection.session()
        cursor.execute(text('delete from reference_table'))
        cursor.commit()


reference_repository = ReferenceRepository(db)
