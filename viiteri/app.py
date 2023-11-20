""" viiteri/app.py """
from flask import Flask

from viiteri.routes import index

app = Flask(__name__)
app.register_blueprint(index.blueprint)


@app.route("/ping")
def pong():
    """ Ponging """
    return "pong"
