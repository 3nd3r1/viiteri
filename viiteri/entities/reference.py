"""viiteri/entities/reference.py"""


# pylint: disable=too-many-instance-attributes

class Reference:

    """Class for representing references (currently only article-type)"""

    def __init__(self, **kwargs):

        if not kwargs.keys() >= {"cite_key", "author", "title", "journal", "year"}:
            raise ValueError("Missing required arguments")

        self.cite_key = kwargs["cite_key"]
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

    @classmethod
    def from_str(cls, content):
        """ Convert content string to Reference object """
        return cls(**eval(content))  # pylint: disable=eval-used
