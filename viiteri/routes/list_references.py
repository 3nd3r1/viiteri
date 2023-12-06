""" viiteri/routes/list_references.py """
from flask import Blueprint, render_template, flash

from viiteri.services.reference_service import reference_service
from viiteri.repositories.reference_repository import DatabaseError


blueprint = Blueprint("list_references", __name__)


@blueprint.route("/list")
def render_list():
    """ Render listing page """
    try:
        references = reference_service.get_all_references()
    except DatabaseError as error:
        flash(str(error), "error")
    return render_template("list.html", references=references)
