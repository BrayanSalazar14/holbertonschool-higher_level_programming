#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as stdrr:
        print("Exception: {}".format(stdrr), file=sys.stderr)
        return None
