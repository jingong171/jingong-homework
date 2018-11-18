from random import randint
"""从外部引入模块"""

class Die():
    """创建骰子的类"""
    def __init__(self):
        """初始化骰子的值为6"""
        self.sides=6

    def roll_dice(self):
        """掷骰子并得到result,打印出1到骰子面之间的随机数"""
        x=randint(1,6)
        for i in range(1,x):
            print(str(i))


die=Die()
for i in range(0,10):
    die.roll_dice()


    



        
    
