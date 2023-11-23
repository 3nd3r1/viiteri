""" viiteri/utils/initialize_db.py """
from sqlalchemy.sql import text

from viiteri.app import db


def drop_table(connection):
    """Deletes the reference table (if existing)"""
    cursor = connection.session()
    cursor.execute(text("""
        DROP TABLE IF EXISTS reference_table;
    """))
    cursor.commit()


def create_table(connection):
    """Creates the reference table"""
    cursor = connection.session()
    cursor.execute(text("""
        CREATE TABLE reference_table (
            id SERIAL PRIMARY KEY,
            content TEXT
        );
    """))
    cursor.commit()


def initialize_database():
    """Initializes database"""
    drop_table(db)
    create_table(db)


if __name__ == "__main__":
    initialize_database()
