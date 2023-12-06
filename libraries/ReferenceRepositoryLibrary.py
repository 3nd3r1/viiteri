""" libraries/ReferenceRepositoryLibrary.py """
# pylint: disable=invalid-name

from viiteri.app import create_app
from viiteri.repositories.reference_repository import reference_repository
from viiteri.utils.initialize_db import initialize_database
from viiteri.utils.reference_factory import ReferenceFactory


class ReferenceRepositoryLibrary:
    """ Library for repository operations """

    def __init__(self):
        self._app = create_app()
        self._repository = reference_repository

    def get_reference_count_in_database(self) -> int:
        """Gets all references from the database"""
        with self._app.app_context():
            return len(self._repository.get_all_references())

    def add_article_to_database(self, title: str, author: str, year: str, journal: str) -> None:
        """Adds a reference to the database"""
        cite_key = title[0:3]+author[0:3]
        with self._app.app_context():
            self._repository.add_reference(
                ReferenceFactory.create_reference("article",
                                                  cite_key=cite_key,
                                                  title=title,
                                                  author=author,
                                                  year=year,
                                                  journal=journal))

    def initialize_database(self):
        """Initializes database"""
        with self._app.app_context():
            initialize_database()
