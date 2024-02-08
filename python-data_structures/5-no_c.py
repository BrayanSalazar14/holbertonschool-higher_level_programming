#!/usr/bin/python3
def no_c(my_string):
    myStringCopy = []
    for i in my_string:
        if i != 'c' and i != 'C':
            myStringCopy.append(i)
    myNewString = ''.join(myStringCopy)
    return myNewString
