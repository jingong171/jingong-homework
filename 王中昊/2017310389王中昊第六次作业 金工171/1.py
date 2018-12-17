import pygal

from random import randint
class Die():
    def __init__(self,num_sides=6):
        self.num_sides=num_sides
    def roll(self):
        return randint(1,self.num_sides)
        
die1=Die()
die2=Die(10)

results=[]
for roll in range(1000):
    result=die1.roll()*die2.roll()
    results.append(result)

frequencies=[]
max_result=die1.num_sides*die2.num_sides
for value in range(1,max_result+1):
    frequency=results.count(value)
    frequencies.append(frequency)

hist=pygal.Bar()
hist.title="摇一个六面骰子和一个十面骰子的结果之积。"
hist.x_labels=[]

for num in range(1,61):
    hist.x_labels.append(num)
##print(hist.x_labels)
##while True:
##    for a in range(0,60):
##        print(a)
##        for i in range(1,7):
##            for n in range(1,11):
##                if int(hist.x_labels[a]) == int(i*n):
##                    break
##        del hist.x_labels[a]
##        break
    
hist.x_title="结果"
hist.y_title="结果的频率"
hist.width=1500
hist.add("D6*D10",frequencies)
hist.render_to_file('dice visual.svg')
    
    
