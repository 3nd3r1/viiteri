""" viiteri/routes/list_references.py """
from flask import Blueprint, render_template, flash, request
from sqlalchemy.exc import SQLAlchemyError

from viiteri.services.reference_service import reference_service


blueprint = Blueprint("list_references", __name__)


@blueprint.route("/list")
def render_list():
    """ Render listing page """
    search_query = request.args.get('search', '').strip()
    sort_type = request.args.get('sort')
    sort_order = request.args.get('order', 'asc')

    try:
        references = reference_service.get_references(sort_type, sort_order, search_query)
    except SQLAlchemyError:
        flash("Database failed to get all references", "error")
        references = []

    return render_template("list.html", references=references, search_query=search_query)
