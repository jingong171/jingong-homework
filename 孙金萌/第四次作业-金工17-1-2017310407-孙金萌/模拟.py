from random import randint
class Die():
    """模拟掷骰子的程序"""

    def __init__(self):
        self.sides = 6

    def roll_die(self):
        x = randint(1,6)
        
        print(x)

die = Die()
print(str(die.sides)+"sides")
for i in range(0,10):
    die.roll_die()
