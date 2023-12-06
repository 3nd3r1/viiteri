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

    def format_bibtex(self):
        """ Return BibTeX formatted reference """
        fields = [
            f"{self.cite_key}",
            f"author = \"{self.author}\"",
            f"title = \"{self.title}\"",
            f"booktitle = \"{self.booktitle}\"",
            f"year = \"{self.year}\"",
            *([f"editor = \"{self.editor}\""] if self.editor else []),
            *([f"volume = \"{self.volume}\""] if self.volume else []),
            *([f"number = \"{self.number}\""] if self.number else []),
            *([f"series = \"{self.series}\""] if self.number else []),
            *([f"pages = \"{self.pages}\""] if self.pages else []),
            *([f"month = \"{self.month}\""] if self.month else []),
            *([f"address = \"{self.address}\""] if self.address else []),
            *([f"organization = \"{self.organization}\""] if self.organization else []),
            *([f"publisher = \"{self.publisher}\""] if self.publisher else []),
            *([f"note = \"{self.note}\""] if self.note else []),
            *([f"annote = \"{self.annote}\""] if self.annote else []),
        ]

        bt_fields = ",\n        ".join(fields)
        return "@inproceedings{" + bt_fields + "\n}"