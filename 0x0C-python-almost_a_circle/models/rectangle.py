#!/usr/bin/python3
"""Module rectangle.
Create a Rectangle class, inheriting from Base.
"""

from models.base import Base


class Rectangle(Base):
    """ The `Rectangle` class
    """
    def __init__(self, width, height, x=0, y=0, id=None):

        """ The constructor of the `Rectangle` class
        Attrs:
            width: a width of a rectangle
            height: a height of a rectangle
            x: the x coordinate
            y: the y coordinate
            id: optional id
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        """getter for width"""
        @property
        def width(self):
            return self.__width

        """setter for width"""
        @width.setter
        def width(self, width):
            if type(width) is not int:
                raise TypeError("width must be an integer")

            if width <= 0:
                raise ValueError("width must be > 0")
            self.__width = width

        """getter for height"""
        @property
        def height(self):
            return self.__height

        """setter for height"""
        @height.setter
        def height(self, height):
            if type(height) is not int:
                raise TypeError("height must be an integer")

            if height <= 0:
                raise ValueError("height must be > 0")
            self.__height = height

        """getter for x"""
        @property
        def x(self):
            return self.__x

        """setter for x"""
        @x.setter
        def x(self, x):
            if type(x) is not int:
                raise TypeError("x must be an integer")

            if x < 0:
                raise ValueError("x must be >= 0")

            self.__x = x

        """getter for y"""
        @property
        def y(self):
            return self.__y

        """setter for y"""
        @y.setter
        def y(self, y):
            if type(y) is not int:
                raise TypeError("y must be an integer")

            if y < 0:
                raise ValueError("y must be >= 0")

            self.__y = y
