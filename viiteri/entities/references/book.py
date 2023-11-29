""" viiteri/entities/references/book.py """

# pylint: disable=too-many-instance-attributes
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
            reference = f"{author[0][0]}. {author[1]}"

        fields = [self.title, self.editor, self.publisher, self.year, self.pages]
        if self.author == self.editor:
            reference += "Ed. "
            fields.remove(self.editor)

        reference += ', '.join(field for field in fields if field)

        return reference
