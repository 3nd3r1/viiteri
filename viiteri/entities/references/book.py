""" viiteri/entities/references/book.py """

from viiteri.entities.references import Reference


class Book(Reference):
    """ Class for representing 'book'-type references """

    def __init__(self, **kwargs):
        if not kwargs.keys() >= {"cite_key", "author", "title", "publisher", "year"}:
            raise ValueError("Missing required arguments")

        super().__init__("book", kwargs["cite_key"])
        self.author = kwargs["author"]
        self.title = kwargs["title"]
        self.publisher = kwargs["publisher"]
        self.year = int(kwargs["year"])

        # Optional arguments
        self.editor = kwargs.get("editor", None)
        self.edition = kwargs.get("edition", None)
        self.volume = kwargs.get("volume", None)
        self.number = kwargs.get("number", None)
        self.pages = kwargs.get("pages", None)
        self.month = kwargs.get("month", None)
        self.series = kwargs.get("series", None)
        self.address = kwargs.get("address", None)
        self.doi = kwargs.get("doi", None)
        self.issn = kwargs.get("issn", None)
        self.isbn = kwargs.get("isbn", None)
        self.note = kwargs.get("note", None)
        self.annote = kwargs.get("annote", None)
