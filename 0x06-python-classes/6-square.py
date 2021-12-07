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
        if isinstance(value, tuple) is False or len(value) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        if not isinstance(value[0], int) or not isinstance(value[1], int):
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
        if self.size is 0:
            print()
        else:
            for j in range(0, self.position[1]):
                print()

            for i in range(0, self.size):
                print(" " * self.position[0] + "#" * self.size)
