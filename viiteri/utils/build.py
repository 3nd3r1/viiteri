""" viiteri/utils/build.py """
from viiteri.utils.initialize_db import initialize_database


def build():
    """Starts the initializing of the database"""
    initialize_database()


if __name__ == "__main__":
    build()
