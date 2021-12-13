#!/usr/bin/python3

"""1-rectangle defines a Rectangle class"""

class Rectangle:
    def __init__(self, width=0, height=0):
        """intialises a rectangle instance.

        Args:
            width: width of the rectangle
            height: height of the rectangle
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """The width property getter"""

        return self.__width

    @width.setter
    def width(self, value):
        """The width property setter"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """The height property getter"""

        return self.__height

    @height.setter
    def height(self, value):
        """the height property setter"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

