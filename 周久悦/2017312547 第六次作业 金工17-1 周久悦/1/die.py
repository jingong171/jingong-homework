from random import randint

class Die():
    def __init__(self,sides=6):
        self.sides=sides

    def roll_die(self):
        """掷骰子"""
        x=randint(1,self.sides) #点数
        return x
