class Die():
    def __init__(self):
        self.sides=6

    def roll_die(self):
        from random import randint
        x=randint(1,6)
        self.sides=x
        print(self.sides)

die_01=Die()
print('6 sides:')
for value in range (10):
    die_01.roll_die()
    
