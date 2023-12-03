""" viiteri/routes/bibtex.py """
from flask import Blueprint, render_template
from viiteri.services.reference_service import reference_service


blueprint = Blueprint("bibtex", __name__)


@blueprint.route("/bibtex")
def render_list():
    """ Render listing page """
    references = reference_service.get_all_references()
    return render_template("bibtex.html", references=references)
