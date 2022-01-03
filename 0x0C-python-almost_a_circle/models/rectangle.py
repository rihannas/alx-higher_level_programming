#!/usr/bin/python3
"""Module rectangle.
Create a Rectangle class, inheriting from Base.
"""

from models.base import Base


class Rectangle(Base):
    """Class describing a rectangle.
    Priavte instance:
        - width
        - height
        - x
        - y
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id=None)

        self.__width = width

        #getter for width
        def get_width(self):
            return self.__width

        #setter for width
        def set_width(self, width):
            self.__width = width


        self.__height = height

        #getter for height
        def get_height(self):
            return self.__height

        #setter for height
        def set_height(self, height):
            self.__height = height

        self.__x = x

        #getter for x
        def get_x(self):
            return self.__x

        #setter for x
        def set_x(self, x):
        self.__x = x

        self.__y = y

        #getter for y
        def get_y(self):
            return self.__y

        #setter for y
        def set_y(self, y):
            self.__y = y

        super().__init__(id)
