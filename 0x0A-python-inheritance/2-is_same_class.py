#!/usr/bin/python3
"""function to see"""


def is_same_class(obj, a_class):
    """check"""
    return (isinstance(obj, a_class) and not type(obj) is a_class)
