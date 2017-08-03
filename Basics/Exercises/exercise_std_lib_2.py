# 03.08.2017
from random import randint


class Die():
    """A simple model of a dice"""

    def __init__(self, sides):
        """Initialize attributes"""
        self.sides = sides

    def roll_die(self):
        """Imitates a roll"""
        roll = randint(1, self.sides)
        print(roll)


dice = Die(6)
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
print("---")

dice = Die(10)
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
print("---")

dice = Die(20)
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
