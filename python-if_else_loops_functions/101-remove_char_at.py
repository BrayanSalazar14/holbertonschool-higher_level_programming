#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0:
        firstLine = str[:n]
        secondLine = str[n+1:]
        return firstLine + secondLine
    else:
        return str
