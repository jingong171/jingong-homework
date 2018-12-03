from random import randint


class Die():
    """创建一个Die类"""
    def __init__(self,sides,times):
        self.sides=6
        self.times=times
          

    def roll_die(self):
        for i in range(1,self.times+1):
            x=randint(1,self.sides)
            print(x)

new_die=Die(6,10)#创建一个实例
new_die.roll_die()
