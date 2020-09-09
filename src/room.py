# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    """Base class for all Rooms.

    :var name: str
    :var description: str


    """

    #  Class Variables

    name = None
    description = None

    def __init__(self, name: str, description: str):

        #  Instance variable:

        self.name = name
        self.description = description

    def __repr__(self):

        """Return the class name and dict of instance variables and their values when printing the instance."""
        return f'{self.__class__} {self.__dict__}'
