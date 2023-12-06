""" viiteri/entities/references/book.py """

# pylint: disable=too-many-instance-attributes, duplicate-code
from viiteri.entities.references import Reference


class Book(Reference):
    """ Class for representing 'book'-type references """

    def __init__(self, **kwargs):
        if not kwargs.keys() >= {"cite_key", "author", "editor", "title", "publisher", "year"}:
            raise ValueError("Missing required arguments")

        super().__init__("book", kwargs["cite_key"])
        self.author = kwargs["author"]
        self.editor = kwargs["editor"]
        self.title = kwargs["title"]
        self.publisher = kwargs["publisher"]
        self.year = kwargs["year"]

        # Optional arguments
        self.number = kwargs.get("number", None)
        self.volume = kwargs.get("volume", None)
        self.pages = kwargs.get("pages", None)
        self.month = kwargs.get("month", None)
        self.note = kwargs.get("note", None)
        self.doi = kwargs.get("doi", None)
        self.issn = kwargs.get("issn", None)
        self.isbn = kwargs.get("isbn", None)

    def format_ieee(self):
        """Returns the reference in IEEE format"""
        author = self.author.split(' ')
        reference = f"{self.author}, "
        if len(author) > 1:
            reference = f"{author[0][0]}. {author[1]}, "

        fields = [self.title, self.editor, self.publisher, self.year, self.pages]
        if self.author == self.editor:
            reference += "Ed. "
            fields.remove(self.editor)

        reference += ', '.join(field for field in fields if field)

        return reference

    def format_bibtex(self):
        """ Return BibTeX formatted reference """
        fields = [
            f"{self.cite_key}",
            f"author = \"{self.author}\"",
            f"editor = \"{self.editor}\"",
            f"title = \"{self.title}\"",
            f"publisher = \"{self.publisher}\"",
            f"year = \"{self.year}\"",
            *([f"number = \"{self.number}\""] if self.number else []),
            *([f"volume = \"{self.volume}\""] if self.volume else []),
            *([f"pages = \"{self.pages}\""] if self.pages else []),
            *([f"month = \"{self.month}\""] if self.month else []),
            *([f"note = \"{self.note}\""] if self.note else []),
            *([f"doi = \"{self.doi}\""] if self.doi else []),
            *([f"issn = \"{self.issn}\""] if self.issn else []),
            *([f"isbn = \"{self.isbn}\""] if self.isbn else []),
        ]

        bt_fields = ",\n        ".join(fields)
        return "@book{" + bt_fields + "\n}"
    