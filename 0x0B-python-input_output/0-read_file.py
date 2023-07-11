#!/usr/bin/python3
"""reading the content of a file"""


def read_file(filename=""):
    """reading the content"""
    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
