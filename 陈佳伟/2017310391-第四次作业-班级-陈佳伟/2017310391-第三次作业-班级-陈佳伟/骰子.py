from random import randint

class Die:
    def __init__(self,sides=6):
        self.sides=sides
    def roll_die(self):
        print(randint(1,self.sides),end=' ')

        
for i in range(10):
    my_die=Die()
    my_die.roll_die()
