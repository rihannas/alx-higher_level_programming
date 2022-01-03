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
        def get_width(self):
            return self.__width

        """setter for width"""
        def set_width(self, width):
            self.__width = width

        """getter for height"""
        def get_height(self):
            return self.__height

        """setter for height"""
        def set_height(self, height):
            self.__height = height

        """getter for x"""
        def get_x(self):
            return self.__x

        """setter for x"""
        def set_x(self, x):
            self.__x = x

        """getter for y"""
        def get_y(self):
            return self.__y

        """setter for y"""
        def set_y(self, y):
            self.__y = y
