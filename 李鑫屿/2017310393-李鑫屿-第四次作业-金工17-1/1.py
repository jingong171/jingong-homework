class Die():
    def __init__(self,sides):
        self.sides=6
    def roll_die(self,sides):##创建随机数
        from random import randint
        x=randint(1,sides)
        print(x)
die1=Die("6")
for i in range(1,11):
    die1.roll_die(6)
    i=i+1
