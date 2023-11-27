""" viiteri/entities/reference/book.py """

# pylint: disable=too-many-instance-attributes
from viiteri.entities.reference import Reference


class Article(Reference):
    """ Class for representing 'book'-type references """

    def __init__(self, **kwargs):
        if not kwargs.keys() >= {"cite_key", "author", "editor", "title", "publisher", "year"}:
            raise ValueError("Missing required arguments")

        super().__init__("article", kwargs["cite_key"])
        self.author = kwargs["author"]
        self.editor = kwargs["editor"]
        self.title = kwargs["title"]
        self.publisher = kwargs["publisher"]
        self.year = kwargs["year"]

        # Optional arguments
        self.volume = kwargs.get("volume", None)
        self.number = kwargs.get("number", None)
        self.pages = kwargs.get("pages", None)
        self.month = kwargs.get("month", None)
        self.note = kwargs.get("note", None)
        self.doi = kwargs.get("doi", None)
        self.issn = kwargs.get("issn", None)
        self.isbn = kwargs.get("isbn", None)
