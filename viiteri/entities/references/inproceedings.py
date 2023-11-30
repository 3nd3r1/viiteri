""" viiteri/entities/references/inproceedings.py """

# pylint: disable=too-many-instance-attributes
from viiteri.entities.references import Reference


class Inproceedings(Reference):
    """ Class for representing 'inproceedings'-type references """

    def __init__(self, **kwargs):
        if not kwargs.keys() >= {"cite_key", "author", "title", "booktitle", "year"}:
            raise ValueError("Missing required arguments")

        super().__init__("inproceedings", kwargs["cite_key"])
        self.author = kwargs["author"]
        self.title = kwargs["title"]
        self.booktitle = kwargs["booktitle"]
        self.year = kwargs["year"]

        # Optional arguments
        self.editor = kwargs.get("editor", None)
        self.volume = kwargs.get("volume", None)
        self.number = kwargs.get("number", None)
        self.series = kwargs.get("series", None)
        self.pages = kwargs.get("pages", None)
        self.month = kwargs.get("month", None)
        self.address = kwargs.get("address", None)
        self.organization = kwargs.get("organization", None)
        self.publisher = kwargs.get("publisher", None)
        self.note = kwargs.get("note", None)
        self.annote = kwargs.get("annote", None)

    def format_ieee(self):
        """Returns the reference in IEEE format"""
        author = self.author.split(' ')
        reference = f"{self.author}, "
        if len(author) > 1:
            reference = f"{author[0][0]}. {author[1]}, "

        fields = [self.title, self.booktitle, self.volume, self.series,
                  self.editor, self.month, self.year, self.pages]

        reference += ', '.join(field for field in fields if field)

        return reference
