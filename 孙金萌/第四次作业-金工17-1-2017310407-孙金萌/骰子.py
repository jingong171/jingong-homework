from random import randint
class Die():
    """docstring for Die"""

    def __init__(self):
        """初始化程序"""
        self.sides = 6

    def roll_die(self):
        """模拟掷骰子"""
        x = randint(1,6)
        self.sides=x
        print(self.sides)

die = Die()
print("6 sides")
for i in range(0,10):
    die.roll_die()
