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

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation
        Args:
            json_string: string representing a list of dictionaries
        """
        if not json_string:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set
        Args:
            cls: the reference to the class
            dictionary: the double pointer to a dictionary
        """
        if cls.__name__ is "Square":
            temp = cls(42)  # can't be called without attributes
        if cls.__name__ is "Rectangle":
            temp = cls(42, 42)  # can't be called without attributes

        temp.update(**dictionary)  # pass the dictionary as a double pointer

        return temp

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances
        Args:
            cls: the reference to the class
        """
        try:
            with open(cls.__name__ + ".json", "r") as a_file:
                content = cls.from_json_string(a_file.read())

                result = []
                for el in content:
                    result.append(cls.create(**el))

                return result

        except FileNotFoundError:
            return []
