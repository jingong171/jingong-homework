from random import randint
class Die():
    def __init__(self,sides):
        self.sides=6
        """设置die，并给默认值6"""
   
    def roll_die(self):
        """设置属性"""
        print("This is"+str(randint(1,self.sides))+"!")
a=Die(6) 

for i in range(1,11):
    a.roll_die()
    """接下来投掷10次"""
