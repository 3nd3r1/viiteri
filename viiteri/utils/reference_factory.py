""" viiteri/utils/reference_factory.py """

from viiteri.entities.reference import Article


class ReferenceFactory:
    """ Factory class for creating references """
    @staticmethod
    def create_reference(reference_type, **kwargs):
        """ Create a reference of given type """
        if reference_type == Article.type:
            return Article(**kwargs)

        raise ValueError("Unknown reference type")

    @staticmethod
    def from_str(content):
        """ Create a reference from string """
        content_dict = eval(content)  # pylint: disable=eval-used
        content_dict["cite_key"] = content_dict.pop("_cite_key")
        return ReferenceFactory.create_reference(content_dict["_type"], **content_dict)
