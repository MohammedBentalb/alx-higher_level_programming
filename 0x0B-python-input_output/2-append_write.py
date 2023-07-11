#!/usr/bin/python3
"""append a text to a file function"""


def append_write(filename="", text=""):
    """use a for append"""
    with open(filename, "a", encoding="UTF-8") as f:
        return f.write(text)
