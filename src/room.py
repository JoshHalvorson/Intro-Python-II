# Implement a class to hold room information. This should have name and
# description attributes.

import random

class Room:
    def __init__(self, name, description, n_to = None, s_to = None, e_to = None, w_to = None):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        self.items = []

    def checkForItems(self):
        s = f'You see these items:\n'
        if len(self.items) > 0:
            for i in self.items:
                s += str(i) + '\n'
        else:
            s = "No items"
        return s

    def addItems(self, items_list):
        if self.items != None:
            self.items.clear()
            for i in range(random.randint(0, 5)):
                self.items.append(items_list[random.randint(0, len(items_list) - 1)])

    def __str__(self):
        return f'Room: {self.name}\nDescription: {self.description}'

    def __repr__(self):
        return f'Room({repr(self.name)}, {repr(self.description)})'

    