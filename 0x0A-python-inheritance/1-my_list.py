#!/usr/bin/python3
"""list class"""


class MyList(list):
    """return sorted list"""
    def print_sorted(self):
        print(sorted(self))
