from room import Room
from player import Player
# Declare all the rooms

# change for first pull reqeust

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

directions = ['north', 'east', 'south', 'west']

player = Player('J the Old', room['outside'])

while True:

    print('You are currently in', player.current_room.name)
    print('................')
    print(player.current_room.description)

    next_dir = input(f'{player.name}... If ye be brave enough; type in your next direction (or if ye be yellow; press q to quit game):\n ')
    

    if next_dir == 'north':
        if player.current_room.n_to:
            player.current_room = player.current_room.n_to
        else:
            print("Can't go that way, please try again brave adventurer!")
    if next_dir == 'east':
        if player.current_room.e_to:
            player.current_room = player.current_room.s_to
        else:
            print("Not a good idea, try again!")
    if next_dir == 'south':
        if player.current_room.s_to:
            player.current_room = player.current_room.e_to
        else:
            print("There's nothing in that direction, try again!")
    if next_dir == 'west':
        if player.current_room.w_to:
            player.current_room = player.current_room.w_to
        else:
            print("Ran into a wall... is that fun for you?")

    if next_dir == 'q':
        exit(0)