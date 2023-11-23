""" viiteri/app.py """
from flask import Flask

from viiteri.routes import index, list_references

app = Flask(__name__)
app.register_blueprint(index.blueprint)
app.register_blueprint(list_references.blueprint)


@app.route("/ping")
def pong():
    """ Ponging """
    return "pong"
