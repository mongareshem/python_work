from collections import OrderedDict
from random import randint

glossary = OrderedDict()

glossary['callable(C)'] = 'includes functions such as range() and len()'
glossary['pointers(P)'] = ('a variable that stores the memory address'
                           ' of another variable')
glossary['pointers'] =  ('python uses object references rather'
                         ' than raw pointers')
glossary['debugging'] = 'the process of finding and fixing errors.'
glossary['breakpoint'] = ('a marker set in code at a specific'
                          ' line to pause program execution for debugging.')

# Notice the brackets are due to multi-line printing

for key, value in glossary.items():
    print(f"{key}: {value.capitalize()}")


class Die:
    """A model of a die"""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(f"\tSide Number: {randint(1, self.sides)}")

die = Die()

print("\n6-Die Results:")
die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()

die_2 = Die(12) #try 10, 20, ...

print("\n12-Die Results:")
die_2.roll_die()
die_2.roll_die()
die_2.roll_die()
die_2.roll_die()
die_2.roll_die()
