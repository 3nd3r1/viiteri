""" viiteri/entities/references/article.py """

# pylint: disable=too-many-instance-attributes
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
        self.note = kwargs.get("note", None)
        self.issn = kwargs.get("issn", None)
        self.zblnumber = kwargs.get("zblnumber", None)
        self.eprint = kwargs.get("eprint", None)

    def format_ieee(self):
        """Returns the reference in IEEE format"""
        author = self.author.split(' ')
        reference = f"{self.author}, "
        if len(author) > 1:
            reference = f"{author[0][0]}. {author[1]}, "

        fields = [self.title, self.journal, self.volume, self.number,
                  self.pages, self.month, self.year, self.doi]

        reference += ', '.join(field for field in fields if field)

        return reference

    def format_bibtex(self):
        """ Return BibTeX formatted reference """
        return f"""@article{{{self.cite_key},
            author = {{{self.author}}},
            title = {{{self.title}}},
            journal = {{{self.journal}}},
            year = {{{self.year}}},
            {{"volume: {self.volume}," if self.volume else None}}
            {{"number: {self.number}," if self.number else None}}
            {{"pages: {self.pages}," if self.pages else None}}
            {{"month: {self.month}," if self.month else None}} 
            {{"doi: {self.doi}," if self.doi else None}} 
            {{"note: {self.note}," if self.note else None}} 
            {{"issn: {self.issn}," if self.issn else None}} 
            {{"zblnumber: {self.zblnumber}," if self.zblnumber else None}} 
            {{"eprint: {self.eprint}," if self.eprint else None}} 
        }}"""