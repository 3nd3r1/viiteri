""" viiteri/entities/references/inproceedings.py """

from viiteri.entities.references import Reference


# pylint: disable=duplicate-code
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
            *([f"organization = \"{self.organization}\""]
              if self.organization else []),
            *([f"publisher = \"{self.publisher}\""] if self.publisher else []),
            *([f"note = \"{self.note}\""] if self.note else []),
            *([f"annote = \"{self.annote}\""] if self.annote else []),
        ]

        bt_fields = ",\n        ".join(fields)
        return "@inproceedings{" + bt_fields + "\n}"
