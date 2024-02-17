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
    for index in range(len(text)):
        if text[index - 1] in listSearch:
            if text[index] != " ":
                textIndent += text[index]
        elif text[index] not in listSearch:
            textIndent += text[index]
        else:
            textIndent += text[index]
            textIndent += "\n" * 2
    print(textIndent, end="")
