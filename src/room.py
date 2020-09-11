# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    """Base class for all Rooms.

    :var name: str
    :var description: str


    """
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __repr__(self):

        """Return the class name and dict of instance variables
        and their values when printing the instance."""
        return f'{self.__class__} {self.__dict__}'
