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
        return fr"""@article{{{self.cite_key},\n
            author = "{self.author}",\n
            title = "{self.title}",\
            journal = "{self.journal}",\n
            year = "{self.year}",\n
            {fr'volume = "{self.volume}",\n' if self.volume else ""}
            {fr'number = "{self.number}",\n' if self.number else ""}
            {fr'pages = "{self.pages}",\n' if self.pages else ""}
            {fr'month = "{self.month}",\n' if self.month else ""} 
            {fr'doi = "{self.doi}",\n' if self.doi else ""}
            {fr'note = "{self.note}",\n' if self.note else ""} 
            {fr'issn = "{self.issn}",\n' if self.issn else ""} 
            {fr'zblnumber = "{self.zblnumber}",\n' if self.zblnumber else ""}
            {fr'eprint = "{self.eprint}",\n' if self.eprint else ""}
        }}"""
        