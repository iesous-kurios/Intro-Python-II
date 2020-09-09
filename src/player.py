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
