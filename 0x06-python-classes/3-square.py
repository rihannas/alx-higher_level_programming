#!/usr/bin/python3
"""respresents a class Square."""


class Square:
    """Represents a square.
    Size: Private object attribute.
    Size attribute: size of a side of the square.
    Instantiation with optional size: def __init__(self, size=0).
    Public instance method: def area(self)."""

    def __init__(self, size=0):
        """Initializes the data."""
        self.__size = size
        if size is not int(size):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise TypeError("size must be >= 0")

    def area(self):
        """Returns square area."""
        result = self.__size * self.__size
        return result
