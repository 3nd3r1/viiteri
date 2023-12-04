# pylint: disable=abstract-class-instantiated

""" viiteri/utils/reference_factory.py """

from viiteri.entities.references import Article, Book, Inproceedings


class ReferenceFactory:
    """ Factory class for creating references """
    @staticmethod
    def create_reference(reference_type, **kwargs):
        """ Create a reference of given type """
        match reference_type:
            case "article":
                return Article(**kwargs)
            case "book":
                return Book(**kwargs)
            case "inproceedings":
                return Inproceedings(**kwargs)

        raise ValueError("Unknown reference type")

    @staticmethod
    def from_str(content):
        """ Create a reference from string """
        content_dict = eval(content)  # pylint: disable=eval-used
        content_dict["cite_key"] = content_dict.pop("_cite_key")
        return ReferenceFactory.create_reference(content_dict["_type"], **content_dict)
