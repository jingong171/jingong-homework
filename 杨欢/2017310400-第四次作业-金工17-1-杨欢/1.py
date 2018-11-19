from random import randint

class Die():
    """编写一个骰子类"""

    def __init__(self,sides=6):
        self.sides=sides
        
    def roll_die(self):
        """随机打印骰子的随机点数"""
        print("您本次的点数为："+str(randint(1,self.sides)))

sides=input("骰子默认为六个面，若要修改，请输入您想要的面数:")
if sides=='':
    ##如果没有输入，则说明不需要改变面数，使用默认方法
    d1=Die()
    print("您的骰子面数为6")
else:
    ##如果输入，则说明需要改变
    sides=int(sides)
    print("您的骰子面数为"+str(sides))
    d1=Die(int(sides))
for i in range(1,11):
    ##掷十次骰子
    d1.roll_die()

