#!/usr/bin/python3
"""class student"""


class Student:
    """set attributes"""

    def __init__(self, first_name, last_name, age):
        """init"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return dict of"""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {item: getattr(self, item) for item in attrs if hasattr(self, item)}
        return self.__dict__
