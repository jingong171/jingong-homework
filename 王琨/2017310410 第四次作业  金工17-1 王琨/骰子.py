class Die():
    def __init__(self,sides=6):#默认值为6
        self.sides=sides

    def roll_die(self):#骰子投出的点数
        from random import randint
        x=randint(1,self.sides)
        return x

side=int(input('Please enter the number of sides of the die:'))
die=Die()#6面骰子
print('The results of the cast:')
for i in range(10):#反复投十次
    print(str(die.roll_die())+' ')
               
