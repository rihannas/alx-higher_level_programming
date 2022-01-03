#!/usr/bin/python3
"""Module base.
Defines a Base class for other classes in the project.
"""


class Base:
    """Class with:
    Private class attribute: __nb_objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization of a Base instance.
        Args:
            - id: id of the instance
        """
        if id is not None:
            self.id = id

        elif id is None:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects
