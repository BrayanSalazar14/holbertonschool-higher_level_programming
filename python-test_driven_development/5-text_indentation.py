#!/usr/bin/python3
"""
This is the "text_indentation" module.
The add module supplies one function, text_indentation().  For example,
>>> text_indentation("hi.")
hi.

"""


def text_indentation(text):
    """Function that prints an text
    function that prints a text with 2 new lines after each of
    these characters: ., ? and :
    """
    textIndent = ""
    if isinstance(text, str):
        for chars in range(len(text)):
            if text[chars - 1] == '.' or text[chars - 1] == '?' or text[chars - 1] == ':':
                if text[chars] != " ":
                    textIndent += text[chars]
            elif text[chars] != '.' and text[chars] != '?' and text[chars] != ':' and text[chars]:
                textIndent += text[chars]
            else:
                textIndent += text[chars]
                textIndent += "\n" * 2
        print(textIndent, end="")
    else:
        raise TypeError("text must be a string")
