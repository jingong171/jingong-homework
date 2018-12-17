#导入模块
from random import randint

class Die():
    def __init__(self,sides=6):
        """initialize attributes to this game"""
        self.sides=sides

    def roll_die(self):
        y=randint(1,self.sides)
        print(y)


die1=Die(6)

for i in range(1,11):
    i=die1.roll_die()
