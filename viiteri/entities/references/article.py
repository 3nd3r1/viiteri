""" viiteri/entities/references/article.py """

# pylint: disable=too-many-instance-attributes, duplicate-code
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
        self.year = kwargs["year"]

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

    def format_bibtex(self):
        """ Return BibTeX formatted reference """
        fields = [
            f"{self.cite_key}",
            f"author = \"{self.author}\"",
            f"title = \"{self.title}\"",
            f"journal = \"{self.journal}\"",
            f"year = \"{self.year}\"",
            *([f"volume = \"{self.volume}\""] if self.volume else []),
            *([f"number = \"{self.number}\""] if self.number else []),
            *([f"pages = \"{self.pages}\""] if self.pages else []),
            *([f"month = \"{self.month}\""] if self.month else []),
            *([f"doi = \"{self.doi}\""] if self.doi else []),
            *([f"issn = \"{self.issn}\""] if self.issn else []),
            *([f"zblnumber = \"{self.zblnumber}\""] if self.zblnumber else []),
            *([f"eprint = \"{self.eprint}\""] if self.eprint else []),
            *([f"note = \"{self.note}\""] if self.note else []),
            *([f"annote = \"{self.annote}\""] if self.annote else []),
        ]

        bt_fields = ",\n        ".join(fields)
        return "@article{" + bt_fields + "\n}"
