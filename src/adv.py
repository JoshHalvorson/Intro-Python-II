from room import Room
from player import Player
from item import Item

# Declare items to be put int rooms
items = [
    Item('Sword', 'A sword'),
    Item('Shield', 'A Shield'),
    Item('Coins', 'Coins'),
    Item('Shovel', 'A Shovel'),
    Item('Book', 'A Book'),
    Item('Health Potion', 'A Health Potion'),
    Item('Spear', 'A Spear'),
    Item('Staff', 'A Staff'),
    Item('Pants', 'A Pants'),
    Item('Helmet', 'A Helmet'),
    Item('Chest Armor', 'Chest Armor'),
    Item('Boots', 'Boots'),
]

# Declare all the rooms

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


def main():
    player = Player('Josh', room['outside'])

    while True:
        player.current_room.addItems(items)
        print(f'\n{player.current_room}')
        print(f'{player.current_room.checkForItems()}')
        room_to_move = input('Select direction to move in (n = north, e = east, s = south, w = west, q = quit): ')
        if room_to_move == 'n':
            if player.current_room.n_to != None:
                player.current_room = player.current_room.n_to
            else:
                print('Cant move in that direction!')
        elif room_to_move == 's':
            if player.current_room.s_to != None:
                player.current_room = player.current_room.s_to
            else:
                print('Cant move in that direction!')
        elif room_to_move == 'e':
            if player.current_room.e_to != None:
                player.current_room = player.current_room.e_to
            else:
                print('Cant move in that direction!')
        elif room_to_move == 'w':
            if player.current_room.w_to != None:
                player.current_room = player.current_room.w_to
            else:
                print('Cant move in that direction!')
        elif room_to_move == 'q':
            break



        

if __name__ == '__main__':
  main()
    