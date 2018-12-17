from random import randint

class Die():
    """模拟骰子"""
    def __init__(self,sides=6):
        """初始化骰子"""
        self.sides=sides

    def roll_die(self):
        """掷骰子"""
        x=randint(1,self.sides)
        print(x)

#创建一个6面骰子
my_six_side_die=Die(6)
#掷10次
for i in range(1,11):
    result=my_six_side_die.roll_die()

