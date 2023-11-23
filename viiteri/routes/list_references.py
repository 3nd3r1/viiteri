# pylint: disable=import-error, no-name-in-module

""" viiteri/routes/list_references.py """
from flask import Blueprint, render_template
from viiteri.services.reference_service import reference_service


blueprint = Blueprint("list_references", __name__)


@blueprint.route("/list")
def render_list():
    """ Render listing page """
    references = reference_service.get_all_references()
    return render_template("list.html", references=references)
