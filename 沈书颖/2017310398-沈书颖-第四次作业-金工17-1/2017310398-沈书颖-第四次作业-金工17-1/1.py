from random import randint
#导入模块random

class Die():

    def __init__(self,sides):
        """初始化骰子的属性"""
        self.sides=6

    def roll_die(self):
        """创建扔骰子的方法"""
        x=randint(1,self.sides)
        print(x)
        
my_die=Die(6)
#创建类的对象，我的骰子

for i in range(1,11):
    i=my_die.roll_die()
#扔十次
