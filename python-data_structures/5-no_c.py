#!/usr/bin/python3
def no_c(my_string):
    """First method with append to insert elements and .join to cancatenate
    myStringCopy = []
    for i in my_string:
        if i != 'c' and i != 'C':
            myStringCopy.append(i)
    myNewString = ''.join(myStringCopy)
    return myNewString
    """
    """Second Method concatenated strings"""
    strCpy = ""
    for chars in my_string:
        if chars != 'c' and chars != 'C':
            strCpy += chars
    return strCpy
