from db import get_database_connection


def drop_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
        DROP TABLE IF EXISTS articles;
    """)
    connection.commit()

def create_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE articles (
            id SERIAL PRIMARY KEY,
            content TEXT
        );
    """)
    connection.commit()

def initialize_database():
    connection = get_database_connection()
    drop_table(connection)
    create_table(connection)


if __name__ == "__main__":
    initialize_database()