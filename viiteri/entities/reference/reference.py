""" viiteri/entities/reference/reference.py """
from abc import ABC


class Reference(ABC):
    """ Abstract class for representing references """

    def __init__(self, reference_type, cite_key):
        self._type = reference_type
        self._cite_key = cite_key

    def __str__(self):
        return str(self.__dict__)

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
    def type(self):
        """ Return reference type """
        return self._type
