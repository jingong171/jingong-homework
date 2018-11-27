from random import randint

class Die():
    def __init__(self,side):
        self.side=side

    def roll_die(self):
        x=randint(1,self.side)
        print(x)

die=Die(6)
for i in range(0,10):
    die.roll_die()
