""" viiteri/routes/index.py """
from flask import (Blueprint, render_template)


blueprint = Blueprint("index", __name__)


@blueprint.route("/")
@blueprint.route("/index")
def render_index():
    """ Render home page """
    return render_template("index.html")
