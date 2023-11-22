""" viiteri/utils/initialize_db.py """
from sqlalchemy.sql import text
from viiteri.utils.db import get_database_connection



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
    connection = get_database_connection()
    drop_table(connection)
    create_table(connection)


if __name__ == "__main__":
    initialize_database()
