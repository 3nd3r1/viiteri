"""viiteri/utils/filter/filter.py"""
from enum import Enum
from viiteri.entities.references import Reference

class Token(Enum):
    """
    Enum to differentiate between different kinds of 
    user input commands in keywords.
    """
    OR      = 2
    AND     = 3

def keyword_filter_references(
        keywords: str, refs: list[tuple[int, Reference]]
        ) -> list[tuple[int, Reference]]:
    """
    Returns a list of references that include the keyword somewhere
    in their string representation. Currently works on the principle 
    that OR (" ") specifies weak keywords, any one of which is enough 
    for a positive result. AND ("&") specifies strong keywords that have 
    to be present for a positive result. 
    """
    tokens = lex_keywords(keywords)
    filtered_refs: list[tuple[int, Reference]] = []
    for ref_id, ref in refs:
        ref_str = ref_dict_to_str(ref.__dict__)
        if is_match(tokens, ref_str.lower()):
            filtered_refs.append((ref_id, ref))
    return filtered_refs

def lex_keywords(keywords: str) -> list[tuple[Token, str]]:
    """
    Goes through the keyword string, and separates and labels
    the different possible commands.
    """
    tokens = []
    split_keywords = keywords.split(",")
    for kw in split_keywords:
        clean_kw = kw.strip()
        if clean_kw[0] == "&":
            tokens.append((Token.AND, clean_kw[1:].lower()))
        else:
            tokens.append((Token.OR, clean_kw.lower()))
    return tokens

def ref_dict_to_str(ref_dict: dict) -> str:
    """
    Translates a Reference entity into a comparable string format.
    """
    values = [str(value) for value in ref_dict.values() if value is not None]
    return " ".join(values)

def is_match(tokens: list[tuple[Token, str]], ref_str: str) -> bool:
    """
    Checks whether a given string adheres to the conditions set by a list of tokens.
    """
    if len(tokens) == 1:
        return tokens[0][1] in ref_str
    match: bool = False
    for token_t, token_v in tokens:
        if token_t == Token.AND:
            match = match and (token_v in ref_str)
        else:
            match = match or (token_v in ref_str)
    return match
