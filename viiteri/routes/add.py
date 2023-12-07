""" viiteri/routes/create_reference.py """

from flask import Blueprint, render_template, redirect, request, flash, session
from sqlalchemy.exc import SQLAlchemyError

from viiteri.services.reference_service import reference_service


blueprint = Blueprint("add", __name__)


@blueprint.route("/add", methods=["GET", "POST"])
def add_reference():
    """ Render page for adding a new reference """
    if request.method == "GET":
        last_ref_type = session.get("last_ref_type", "article")
        return render_template("add.html", last_ref_type=last_ref_type)
    if request.method == "POST":
        ref_type = request.form.get("ref_type")
        try:
            cite_key = request.form["title"][0:3] + \
                request.form["author"].split(" ")[0][0:3]
            reference_service.create_reference(
                ref_type, cite_key=cite_key, **request.form.to_dict())
            flash("Reference created successfully!", "success")
            session["last_ref_type"] = ref_type
        except SQLAlchemyError:
            flash("Database failed to add reference", "error")
        except ValueError as error:
            flash(str(error), "error")
    return redirect("/add")
