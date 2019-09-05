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
    Item('Spear', 'A Spear'),
    Item('Staff', 'A Staff'),
    Item('Pants', 'A Pants'),
    Item('Helmet', 'A Helmet'),
    Item('Boots', 'Boots'),
    Item('Potion', 'A Potion'),
    Item('Armor', 'Armor'),
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

for r in room.values():
    r.addItems(items)

def main():
    player = Player('Josh', room['outside'])
    print('\nHere is a list of commands, type "help" to see them again')
    print(help())
    while True:
        print('\n-------------------------------')
        print(f'\n{player.current_room}')
        command = input('\nEnter a command: ')
        if command.lower() == 'n':
            if player.current_room.n_to != None:
                player.current_room = player.current_room.n_to
            else:
                print('\nCant move in that direction!')
        elif command.lower() == 's':
            if player.current_room.s_to != None:
                player.current_room = player.current_room.s_to
            else:
                print('\nCant move in that direction!')
        elif command.lower() == 'e':
            if player.current_room.e_to != None:
                player.current_room = player.current_room.e_to
            else:
                print('\nCant move in that direction!')
        elif command.lower() == 'w':
            if player.current_room.w_to != None:
                player.current_room = player.current_room.w_to
            else:
                print('\nCant move in that direction!')
        elif len(command.split(' ')) > 1:
            parts = command.split(' ')
            if parts[0].lower() == 'take' or parts[0].lower() == 'get':
                for i in items:
                    if i.name.lower() == parts[1].lower():
                       if i in player.current_room.items:
                           print(player.on_take(i))
                           player.current_room.items.remove(i)
            elif parts[0].lower() == 'drop':
                for i in items:
                    if i.name.lower() == parts[1].lower():
                       if i in player.items:
                           print(player.on_drop(i))
                           player.current_room.items.append(i)
        elif command.lower() == 'i':
            print(f'\n{player.get_items()}')
        elif command.lower() == 'search':
            print(f'\n{player.current_room.checkForItems()}')
        elif command.lower() == 'q':
            break

def help():
    return ''' 
    n - north
    e - east
    s - south
    w - west
    i - inventory
    q - quit
    search - searches room for items
    take "item name" - picks an item up
    drop "item name" - drops an item
    help - shows help'''

if __name__ == '__main__':
  main()
    