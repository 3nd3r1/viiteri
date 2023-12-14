""" viiteri/app.py """
import os
from flask import Flask
from dotenv import load_dotenv

from viiteri.routes import add, list_references, bibtex, remove
from viiteri.utils.db import db

load_dotenv()


def create_app():
    """ Flask app factory """
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
    app.config["SECRET_KEY"] = os.urandom(12).hex()

    db.init_app(app)

    with app.app_context():
        app.register_blueprint(add.blueprint)
        app.register_blueprint(list_references.blueprint)
        app.register_blueprint(bibtex.blueprint)
        app.register_blueprint(remove.blueprint)

        @app.route("/ping")
        def ping():
            """ pong """
            return "pong"

        return app
