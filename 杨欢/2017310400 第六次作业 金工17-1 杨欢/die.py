from random import randint

class Die():
    """建立一个骰子类"""

    def __init__(self,num_sides=6):
        """构造函数，默认骰子有六面"""
        self.num_sides=num_sides

    def roll_dies(self):
        """随机投出一个数"""
        return randint(1,self.num_sides)
    
