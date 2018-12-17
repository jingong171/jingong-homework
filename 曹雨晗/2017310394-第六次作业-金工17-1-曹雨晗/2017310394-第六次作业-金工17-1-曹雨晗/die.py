from random import randint

class Die():
#创建一个表示骰子的类

    def __init__(self, num_sides=6):
    #设定骰子的基本面数为6面
        self.num_sides = num_sides

    def roll(self):
    #返回骰子投掷出来的值
        return randint(1, self.num_sides)
        
