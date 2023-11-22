""" viiteri/routes/create_reference.py """
from flask import Blueprint, render_template, redirect, request, flash
from viiteri.services.reference_service import reference_service


blueprint = Blueprint("create_reference", __name__)


@blueprint.route("/create", methods=["GET", "POST"])
def render_create():
    """ Render create page """
    if request.method == "GET":
        return render_template("create.html")
    if request.method == "POST":
        cite_key = request.form["cite_key"]
        fields = [("author", request.form["author"]), ("title", request.form["title"]),
                  ("journal", request.form["journal"]), ("year", request.form["year"]),
                  ("volume", request.form["volume"])]
        try:
            reference_service.create_reference(cite_key, fields, 'article')
            flash("Reference created successfully!")
        except Exception as error:
            flash(str(error))
    return redirect("/create")
