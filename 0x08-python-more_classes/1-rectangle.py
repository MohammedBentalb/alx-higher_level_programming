#!/usr/bin/python3
"""class that define the with and hight of a rectangle"""


class Rectangle:
    """init method"""
    def __init__(self, width=0, height=0):
        """setting value"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """return a value"""
        return self.__width

    @width.setter
    def width(self, value):
        """setting value that is above 0"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """return the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting a value for height that is higher than 0"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
