"""viiteri/entities/reference.py"""


# pylint: disable=too-many-instance-attributes

class Reference:

    """Class for representing references (currently only article-type)"""

    def __init__(self, **kwargs):

        if ("cite_key", "title", "author", "journal", "year") not in kwargs:
            raise ValueError("Missing required arguments")

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
        self.note = kwargs.get("note", None)
        self.issn = kwargs.get("issn", None)
        self.zblnumber = kwargs.get("zblnumber", None)
        self.eprint = kwargs.get("eprint", None)

    def __str__(self):
        return self.__dict__.__str__()
