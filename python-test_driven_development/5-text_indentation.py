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
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    listSearch = [".", "?", ":"]
    textIndent = ""
    copy = ""
    for chars in text:
        if chars not in listSearch:
            if chars == " " and copy in listSearch:
                copy = ""
                continue
            textIndent += chars
            continue
        copy = chars
        textIndent += chars
        textIndent += "\n" * 2
    print(textIndent, end="")
