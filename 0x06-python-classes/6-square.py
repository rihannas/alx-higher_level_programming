#!/usr/bin/python3
"""module defines a Square class"""


class Square:
    """class that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializer the data."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves size."""

        return self.__size

    @size.setter
    def size(self, value):
        """Sets size to a value."""
        if isinstance(value, int) is not True:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """Retrieves the position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position to a value."""
        if len(value) < 2:
            raise IndexError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """area of square."""
        result = self.__size * self.__size
        return result

    def my_print(self):
        """Prints the square with the character #"""
        if self.__size == 0:
            print()
            return

        if self.__position[1] > 0:
            for n in range(0, self.__position[1]):
                print()

        for i in range(0, self.__size):

            print(" " * self.__position[0] + "#" * self.__size)


my_square = Square(0, (10, 3))
my_square.my_print()
