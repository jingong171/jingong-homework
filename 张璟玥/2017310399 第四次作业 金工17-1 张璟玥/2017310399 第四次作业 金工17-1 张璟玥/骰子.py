from random import randint

class die():
    def __init__(self,sides=6):
        #初始化骰子
        self.sides=sides
    def roll_die(self):   
        x=randint(1,self.sides)#生成随机点数
        print('你掷出的点数为'+str(x))#打印
        

die1=die()
die1.roll_die()
die1.roll_die()
die1.roll_die()
die1.roll_die()
die1.roll_die()
die1.roll_die()
die1.roll_die()
die1.roll_die()
die1.roll_die()
die1.roll_die()





