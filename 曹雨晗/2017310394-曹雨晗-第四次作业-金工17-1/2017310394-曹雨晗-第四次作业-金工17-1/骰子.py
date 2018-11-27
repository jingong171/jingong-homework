class Die():
    def __init__(self,sides):#规定骰子的面数以及默认面数
        self.sides=6

    def roll_die(self):#编写一个摇骰子的方法
        from random import randint
        x=randint(1,self.sides)
        print(x)

die=Die("6")#定义一个骰子的类
for i in range(1,11):
    die.roll_die()
    i=i+1
