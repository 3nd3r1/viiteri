""" viiteri/routes/list_references.py """
from flask import Blueprint, render_template, flash
from sqlalchemy.exc import SQLAlchemyError

from viiteri.services.reference_service import reference_service


blueprint = Blueprint("list_references", __name__)


@blueprint.route("/list")
def render_list():
    """ Render listing page """
    references = []
    try:
        references = reference_service.get_sorted_references()
    except SQLAlchemyError:
        flash("Database failed to get all references", "error")
    return render_template("list.html", references=references)
