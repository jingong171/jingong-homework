from random import randint
class die():
    def __init__(self,sides=6):
        self.sides=sides
    def roll_die(self):
        print(randint(1,self.sides))
my_die=die()
numbers=10
while numbers>0:
    my_die.roll_die()
    numbers=numbers-1
