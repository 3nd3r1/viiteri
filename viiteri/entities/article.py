"""viiteri/entities/article.py"""
class Article:
    """Class for article-type references"""
    def __init__(self, author, title, journal, year, volume):
        self.author = author
        self.title = title
        self.journal = journal
        self.year = year
        self.volume = volume
