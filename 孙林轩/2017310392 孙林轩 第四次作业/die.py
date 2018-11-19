from random import randint
class Die():
    def __init__(self,sides):
        """骰子类构造函数"""
        self.sides=6

    def roll_die(self):
        """扔骰子"""
        print(randint(1,self.sides))
Die1=Die(6)
Die1.roll_die()