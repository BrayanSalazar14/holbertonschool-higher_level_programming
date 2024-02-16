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
    
    textIndent = ""
    for index in range(len(text)):
        chars = text[index]
        lastChars = text[index - 1]
        if lastChars == '.' or lastChars == '?' or lastChars == ':':
            if chars != " ":
                textIndent += chars
        elif chars != '.' and chars != '?' and chars != ':' and chars:
            textIndent += chars
        else:
            textIndent += chars
            textIndent += "\n" * 2
    print(textIndent, end="")
