""" viiteri/utils/db.py """
import os
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from viiteri.app import app


load_dotenv()

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
db = SQLAlchemy(app)

app.app_context().push()

def get_database_connection():
    """Connects database"""
    return db
