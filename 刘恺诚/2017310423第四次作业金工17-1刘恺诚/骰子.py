class Die():
    """A small Die"""
    def __init__(self,sides=6):
        self.sides=sides

    def roll_die(self):
        print(int(randint(1,self.sides)))


from random import randint
sides=int(input("请输入骰子的面数"))
myDie=Die(sides)

for i in range(1,11):
    myDie.roll_die()
    

        
