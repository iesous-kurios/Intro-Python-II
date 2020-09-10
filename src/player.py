# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    """Base class for all Players
       
    :var name: str
    :var current room: str

    Methods:

    - Move North
        - Attempts to move north one position
        - Prints outcome of attempt
        - If move successful, moves Player to new room North of current location
        - If moved to new room, prints player's new location

    - Move East
        - Attempts to move east one position
        - Prints outcome of attempt
        - If move successful, moves Player to new room East of current location
        - If moved to new room, prints player's new location

    - Move South
        - Attempts to move south one position
        - Prints outcome of attempt
        - If move successful, moves Player to new room South of current location
        - If moved to new room, prints player's new location    

    - Move West
        - Attempts to move west one position
        - Prints outcome of attempt
        - If move successful, moves Player to new room West of current location
        - If moved to new room, prints player's new location    

    """

    #  Class Variables

    name = None
    room = None

    def __init__(self, name: str, current_room: str):

        #  Instance variable    
        
        self.name = name
        self.current_room = current_room

    def __repr__(self):
        """Return the class name and dict of instance variables and their values when printing the instance."""
        return f'{self.__class__} {self.__dict__}'

    def __str__(self):
        player_location = f"Player is in the {self.current_room}"    

    def move_direction(self, direction):
        next_room = self.current_room
        
        if next_room is not None:
            self.current_room = next_room

        else:
            print('Sorry, no room in that direction')    
 