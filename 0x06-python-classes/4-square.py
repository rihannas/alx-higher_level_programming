#!/usr/bin/python3
"""respresents a class Square."""


class Square:
    """Represents a square.
    Size attribute: size of a side of the square.
    Private instance attribute: size:
    - property def size(self)
    - property setter def size(self, value)
    Instantiation with optional size: def __init__(self, size=0)
    Public instance method: def area(self)"""

    def __init__(self, size=0):
        """Initializes the data."""
        self.__size = size

    @property
    def size(self):
        """Retrieves  size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets size to a value."""
        if self.__size is not int(self.__size):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise TypeError("size must be >= 0")

        self.__size = value

    def area(self):
        """Returns square area."""
        result = self.__size * self.__size
        return result
