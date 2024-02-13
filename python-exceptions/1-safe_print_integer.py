#!/usr/bin/python3
def safe_print_integer(value):
    try:
        check = int(value)
        print("{:d}".format(check))
    except ValueError:
        return False
    else:
        return True
