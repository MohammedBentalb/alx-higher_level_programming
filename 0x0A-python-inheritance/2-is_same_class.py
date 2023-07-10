#!/usr/bin/python3
"""function to see"""


def is_same_class(obj, a_class):
    """check"""
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    return False
