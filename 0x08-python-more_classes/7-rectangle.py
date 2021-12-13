#!/usr/bin/python3
"""Module 1-rectangle
Defines a Rectangle class.
"""


class Rectangle:
    """Rectangle class defined by width and height.
    Attributes:
        Public class attribute number_of_instances:
        Initialized to 0
        Incremented during each new instance instantiation
        Decremented during each instance deletion"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance.
        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieves the width of a Rectangle instance."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of a Rectangle instance
        Args:
            value: value of the width, must be a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of a Rectangle instance."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of a Rectangle instance
        Args:
            value: value of the height, must be a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of rectangle
        Returns: Area of rectange"""

        area = self.__width * self.__height

        return area

    def perimeter(self):
        """Calculates the perimeter of rectangle
        Returns: Perimeter of rectangle"""

        if self.__width == 0 or self.__height == 0:
            return 0

        perimeter = (2 * self.__width) + (2 * self.__height)

        return perimeter

    def __str__(self):
        """
        Prints the rectangle represented by the combinations of
        the `#` character.
        """
         if self.__width == 0 or self.__height == 0:
            return ""
        string_r = ''
        for i in range(self.__height):
            for j in range(self.__width):
                string_r += str(self.print_symbol)
            if i < (self.height - 1):
                string_r += '\n'
        return string_r

    def __repr__(self):
        """Return a string representation of a Rectangle instance
        that is able to recreate a new instance by using eval()
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Deletes a Rectangle."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
