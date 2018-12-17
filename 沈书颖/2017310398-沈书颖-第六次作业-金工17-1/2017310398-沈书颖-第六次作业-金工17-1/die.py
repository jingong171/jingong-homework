from random import randint
#导入模块random

class Die():

    def __init__(self,sides=6):
        """初始化骰子的属性"""
        self.sides=sides

    def roll(self):
        """创建扔骰子的方法"""
        return randint(1,self.sides)
        
