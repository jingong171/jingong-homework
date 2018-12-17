from random import randint

class Die():
    """骰子类，可以打印1和骰子个数中的随机数"""
    def __init__(self,sides=6):
        self.sides=sides

    def roll_die(self):
        """实现掷骰子并打印出来"""
        x=randint(2,self.sides-1)
        print(str(x))

#Die类的实例
for i in range(1,11):
    Roll_die=Die()
    Roll_die.roll_die()
