""" viiteri/routes/remove.py """
from flask import Blueprint, redirect, request, flash
from sqlalchemy.exc import SQLAlchemyError
from viiteri.services.reference_service import reference_service


blueprint = Blueprint("remove", __name__)


@blueprint.route("/remove", methods=["POST"])
def remove_reference():
    """ Remove reference from database """
    if "reference_id" in request.form:
        ref_id = request.form.get("reference_id")
        try:
            reference_service.remove_reference(ref_id)
            flash("Reference removed successfully!", "success")
        except SQLAlchemyError:
            flash("Database failed to remove reference", "error")
    return redirect("/list")
