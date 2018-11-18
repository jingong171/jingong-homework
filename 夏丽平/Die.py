from random import randint
##定义一个骰子类，可自由决定骰子面数
class Die:
    """定义一个骰子"""
    def __init__(self,sides = 6):
        self.sizes = sides

    def roll_die(self,dot=0):
        dot = randint(1,self.sizes)
        print("the dot of your rolling is "+str(dot)+".")
##主函数实现
m = input("请输入骰子面数")
m = int(m)
die1 = Die(m)
n  = input("请输入投掷次数")
n = int(n)
for i in range(0,n):
    die1.roll_die()
