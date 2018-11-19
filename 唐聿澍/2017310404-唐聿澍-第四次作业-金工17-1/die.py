from random import randint#载入随机库

class Die():#创建骰子类
    def __init__(self,sides = 6):
            self.sides = sides

    def roll_die(self):
        x = randint(1,self.sides)
        return x

list1 = []#创建储存列表
die = Die()
for i in range(1,11):
    result = die.roll_die()
    list1.append(result)

for l in list1:#遍历输出列表
    print(l)
