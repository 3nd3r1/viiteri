"""viiteri/utils/filter/filter.py"""
from enum import Enum
from viiteri.entities.references import Reference

class Token(Enum):
    """
    Enum to differentiate between different kinds of 
    user input commands in keywords.
    """
    KEYWORD = 1
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
    for ref in refs:
        fits: bool = False
        (_, ref_content) = ref
        for i, token in enumerate(tokens):
            (token_type, _) = token
            match token_type:
                case Token.AND:
                    (_, token_content) = tokens[i + 1]
                    if token_content in str(ref_content):
                        fits = True
                        continue
                    fits = False
                    break
                case Token.OR:
                    (_, token_content) = tokens[i + 1]
                    if token_content in str(ref_content):
                        fits = True
                case _:
                    continue
        if fits:
            filtered_refs.append(ref)

    return filtered_refs

def lex_keywords(keywords: str) -> list[tuple[Token, str]]:
    """
    Goes through the keyword string, and separates and labels
    the different possible commands.
    """
    token_list = []
    token_cursor = 0
    token_found = False
    if keywords[0] != "&":
        token_list.append((Token.OR, "OR"))
    for i, _ in enumerate(keywords):
        if token_found: # Skip over the operator token
            token_found = False
            continue

        if keywords[i] == " ":
            token_list.append((Token.KEYWORD, keywords[token_cursor:i].lower()))
            token_list.append((Token.OR, "OR"))
            token_cursor = i + 1
        elif keywords[i] == "&":
            token_list.append((Token.KEYWORD, keywords[token_cursor:i].lower()))
            token_list.append((Token.AND, "AND"))
            token_cursor = i + 1
        else:
            continue

    token_list.append((Token.KEYWORD, keywords[token_cursor:].lower()))
    return token_list
