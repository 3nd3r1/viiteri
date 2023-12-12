""" viiteri/entities/references/reference.py """
from abc import ABC


class Reference(ABC):
    """ Abstract class for representing references """

    def __init__(self, reference_type, cite_key):
        self._type = reference_type
        self._cite_key = cite_key

    def __str__(self):
        return str(self.__dict__)

    def format_bibtex(self):
        """Return BibTeX formatted reference."""
        formatted_rows = [f"@{self.type}{{{self.cite_key},"]

        for field, value in self.__dict__.items():
            if not value or field.startswith("_"):
                continue

            value_str = '"' + value + '"' if isinstance(value, str) else value
            formatted_rows.append(f"    {field} = {value_str},")

        formatted_rows[-1] = formatted_rows[-1][:-1]  # Remove last comma
        formatted_rows.append("}")

        return "\n".join(formatted_rows)

    @property
    def cite_key(self):
        """ Return cite key """
        return self._cite_key

    @property
    def type(self):
        """ Return reference type """
        return self._type
