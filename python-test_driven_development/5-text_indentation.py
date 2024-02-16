#!/usr/bin/python3
"""
This is the "text_indentation" module.
The add module supplies one function, text_indentation().  For example,
>>> text_indentation("hi.")
hi.

"""


def text_indentation(text):
    """Function that prints a text with 2 new lines after each of
    these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = []
    for index, char in enumerate(text):
        if index == 0 or text[index - 1] not in ['.', '?', ':']:
            result.append(char)
        elif char != " ":
            result.append(char)
        if char in ['.', '?', ':']:
            result.append("\n" * 2)

    print(''.join(result), end="")
