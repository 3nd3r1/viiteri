""" viiteri/entities/references/article.py """

from viiteri.entities.references import Reference


class Article(Reference):
    """ Class for representing 'article'-type references """

    def __init__(self, **kwargs):
        if not kwargs.keys() >= {"cite_key", "author", "title", "journal", "year"}:
            raise ValueError("Missing required arguments")

        super().__init__("article", kwargs["cite_key"])
        self.author = kwargs["author"]
        self.title = kwargs["title"]
        self.journal = kwargs["journal"]
        self.year = int(kwargs["year"])

        # Optional arguments
        self.volume = kwargs.get("volume", None)
        self.number = kwargs.get("number", None)
        self.pages = kwargs.get("pages", None)
        self.month = kwargs.get("month", None)
        self.doi = kwargs.get("doi", None)
        self.issn = kwargs.get("issn", None)
        self.zblnumber = kwargs.get("zblnumber", None)
        self.eprint = kwargs.get("eprint", None)
        self.note = kwargs.get("note", None)
        self.annote = kwargs.get("annote", None)
