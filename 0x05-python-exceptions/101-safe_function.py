#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        new = fct(*args)
    except Exception as e:
        sys.stderr.write("Eception: {}\n".format(e))
        return None
    return new
