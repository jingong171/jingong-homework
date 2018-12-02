#一个有关骰子的类
from random import randint

class Die():
    def __init__(self):
        self.sides = 6
        """默认值是6"""        

    def roll_die(self):
        """产生随机数"""
        print("这次的点数是：")
        y=randint(1,self.sides)
        print(y)
      

#产生10次随机数
my_die = Die()
print("骰子默认有"+str(my_die.sides)+"面")
x=0
while(x<10):
    my_die.roll_die()
    x = x+1
    
