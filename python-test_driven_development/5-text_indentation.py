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
        for chars in text:
            if chars != '.' and chars != '?' and chars != ':':
                textIndent += chars
            else:
                textIndent += chars
                textIndent += "\n" * 2
        print(textIndent, end="")
    else:
        raise TypeError("text must be a string")
