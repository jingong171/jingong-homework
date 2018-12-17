from random import randint#随机

class Die():#骰子类
    def __init__(self,sides=6):
        self.sides=sides

    def roll(self):
        return randint(1,self.sides)#返回点数
