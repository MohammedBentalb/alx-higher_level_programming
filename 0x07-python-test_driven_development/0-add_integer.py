#!/bin/usr/python3
"""addition function"""


def add_integer(a, b=98):
    """return integer ddition of a and b either floats or integers"""
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
