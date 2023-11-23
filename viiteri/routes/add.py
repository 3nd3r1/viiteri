# pylint: disable=import-error, no-name-in-module, broad-except

""" viiteri/routes/create_reference.py """
from flask import Blueprint, render_template, redirect, request, flash, session
from viiteri.services.reference_service import reference_service


blueprint = Blueprint("add", __name__)


@blueprint.route("/add", methods=["GET", "POST"])
def add_reference():
    """ Render page for adding a new reference """
    if request.method == "GET":
        submitted = session.pop('submitted', False)
        return render_template("add.html", submitted=submitted)
    if request.method == "POST":
        cite_key = request.form["cite_key"]
        fields = [("author", request.form["author"]),
                  ("title", request.form["title"]),
                  ("journal", request.form["journal"]),
                  ("year", request.form["year"]),
                  ('journal', request.form.get('journal', '')),
                  ('year', request.form.get('year', '')),
                  ('volume', request.form.get('volume', '')),
                  ('number', request.form.get('number', '')),
                  ('pages', request.form.get('pages', '')),
                  ('month', request.form.get('month', '')),
                  ('doi', request.form.get('doi', '')),
                  ('note', request.form.get('note', '')),
                  ('issn', request.form.get('issn', '')),
                  ('zblnumber', request.form.get('zblnumber', '')),
                  ('eprint', request.form.get('eprint', ''))]
        fields = list(filter(lambda x: x[1] != '', fields))
        try:
            reference_service.create_reference(cite_key, fields, 'article')
            flash("Reference created successfully!")
            session["submitted"] = True
        except Exception as error:
            flash(str(error))
            session["submitted"] = False
    return redirect("/add")
