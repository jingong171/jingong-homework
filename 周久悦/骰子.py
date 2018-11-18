from random import randint

class Die():
    def __init__(self,sides=6):
        self.sides=sides

    def roll_die(self):
        """掷骰子"""
        x=randint(1,self.sides) #点数
        print(x)


print("先创建一个6面骰子")
die1=Die()   
print("投骰子：")
die1.roll_die()

for i in range(10):  #再投10次
    sides=int(input("请输入骰子的面数：\t"))
    die=Die(sides)
    print("投骰子：")
    die.roll_die()
