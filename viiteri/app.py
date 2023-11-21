""" viiteri/app.py """
from flask import Flask

from viiteri.routes import index, create_reference

app = Flask(__name__)
app.register_blueprint(index.blueprint)
app.register_blueprint(create_reference.blueprint)


@app.route("/ping")
def pong():
    """ Ponging """
    return "pong"
