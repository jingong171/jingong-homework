from random import randint
class Die():
    """sides为骰子面数，times为投掷次数"""
    def __init__(self,sides=6,times=0):
        self.sides=sides
        self.times=times

    def roll_die(self):
        x = randint(1,int(self.sides))
        print("You get a "+"'"+str(x)+"'.")

    def consistant_rolling(self):
        for i in range(0,int(self.times)):
            y = randint(1,int(self.sides))
            print("You get a "+"'"+str(y)+"'.")


new_die = Die(6,10)
new_die.consistant_rolling()

