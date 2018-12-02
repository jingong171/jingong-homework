from random import randint           #导入randint函数

class Die():                         #定义Die类
    def __init__(self,sides=6):      #面数默认值为6
        self.sides=sides
    def roll_die(self):              #定义掷骰子函数
        print(randint(1,self.sides)) #利用randint输出

die=Die(6)                           #创建一个六面骰子的实例die
for i in range(1,11):
    die.roll_die()
