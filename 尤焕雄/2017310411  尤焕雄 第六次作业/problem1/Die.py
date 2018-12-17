from random import randint
#建立骰子类
class die():
    def __init__(self,x=6):
        self.face=x

    def roll(self):
        return randint(1,self.face)
