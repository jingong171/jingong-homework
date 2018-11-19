from random import randint
"""该模块中标包含一个名为Die的类"""

class Die():
    """该类中包含一个名为sides的属性，用户调用该类，输入该属性值后即生成一个随机值"""
    def __init__(self,sides):
        self.sides=sides #用于存储用户输入的数
        self.result=0 #初始化结果

    def roll_die(self): #该方法用于生成一个随机数
        self.result=randint(1,self.sides)
        print(self.result) #打印生成的随机数

die=Die(6)
for i in range(1,11): #执行十次掷骰子的行为
    die.roll_die()
    
