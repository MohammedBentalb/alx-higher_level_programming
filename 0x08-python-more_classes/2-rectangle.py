#!/usr/bin/python3
"""class define the area and perimeter of rectangle"""


class Rectangle:
    """ init method """
    def __init__(self, width=0, height=0):
        """ setting value to width and height attributes"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """return width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setting value above 0 to width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """return heigth"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting value above 0 to height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__height * self.__width)

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return (2 * (self.__height + self.__width))
