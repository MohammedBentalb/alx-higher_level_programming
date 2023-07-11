#!/usr/bin/python3
"""writing iside the file"""


def write_file(filename="", text=""):
    """return the number of chars writen"""
    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(text)
