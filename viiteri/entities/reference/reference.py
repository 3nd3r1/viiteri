""" viiteri/entities/reference/reference.py """
from abc import ABC, ABCMeta, abstractmethod


class Reference(ABC, metaclass=ABCMeta):
    """ Abstract class for representing references """

    def __init__(self, cite_key):
        self._cite_key = cite_key

    def __str__(self):
        return str({**{"_type": self.type}, **self.__dict__})

    # @abstractmethod
    # def format_ieee(self):
    #    """ Return IEEE formatted reference """

    # @abstractmethod
    # def format_bibtex(self):
    #    """ Return BibTeX formatted reference """

    @property
    def cite_key(self):
        """ Return cite key """
        return self._cite_key

    @property
    @abstractmethod
    def type(self):
        """ Return reference type """
