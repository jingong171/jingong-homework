from random import randint          

class Die():
    """创建一个Die 类"""
    def __init__(self,sides=""):     #Die类的构造函数
        if sides:
            self.sides=sides
        else:
            self.sides=6

    def roll_dies(self):            #编写一个名为roll_die() 的方法，它打印位于1和骰子面数之间的随机数
        return randint(1,self.sides)


die1=Die()
#创建一个6面的骰子

for i in range(1,11):               #掷骰子10次并一次输出结果
    print("第"+ str(i) +"次掷骰子结果为 "+str(die1.roll_dies()))
    
