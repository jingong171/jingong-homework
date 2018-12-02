from random import randint
#导入模块random中生成随机数的函数

class Die():
    """打印位于1和骰子面数之间的随机数"""

    def __init__(self,sides=6):
        self.sides = sides
    """创建一个名为sides（面数）的属性"""

    def roll_die(self):
        print("面数为"+str(self.sides)+"的骰子投掷十次的结果为：",end=' ')
        for i in range(10):
            print(str(randint(1,self.sides))+",",end=' ')
    """打印位于1和骰子面数之间的随机数"""

#创建对象：不同面数的骰子,并打印十个随机数
dice1=Die()
dice1.roll_die()
