""" viiteri/routes/list_references.py """
from flask import Blueprint, render_template
from viiteri.services.reference_service import reference_service
from viiteri.entities.references import Article, Book, Inproceedings


blueprint = Blueprint("list_references", __name__)


@blueprint.route("/list")
def render_list():
    """ Render listing page """
    references = reference_service.get_all_references()
    articles, books, inproceedings = [], [], []

    for ref in references:
        if isinstance(ref, Article):
            articles.append(ref)
        elif isinstance(ref, Book):
            books.append(ref)
        elif isinstance(ref, Inproceedings):
            inproceedings.append(ref)

    return render_template("list.html", articles=articles, books=books, inproceedings=inproceedings)
