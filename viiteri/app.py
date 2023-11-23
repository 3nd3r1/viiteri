""" viiteri/app.py """
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
app.secret_key = os.urandom(12).hex()

db = SQLAlchemy(app)
app.app_context().push()


@app.route("/ping")
def ping():
    """ pong """
    return "pong"
