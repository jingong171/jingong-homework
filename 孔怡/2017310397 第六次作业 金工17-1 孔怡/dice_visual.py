import pygal

from random import randint

class Die():
    def __init__(self,num_sides=6):
        self.num_sides=num_sides
    def roll(self):
        return randint(1,self.num_sides)

die_1=Die()
die_2=Die(10)

results=[]
for roll_num in range(5000):
    result=die_1.roll()*die_2.roll()
    results.append(result)

x=[]
frequencies=[]
max_result=die_1.num_sides * die_2.num_sides
for value in range(1,max_result+1):
    if value in results:
        x.append(value)
        frequency=results.count(value)
        frequencies.append(frequency)
    else:
        continue
        
        
hist=pygal.Bar()

hist.title="掷5000次6面骰子和10面的骰子，点数相乘的结果"
hist.x_labels=x
hist.x_title="Result"
hist.y_title="Frequency of results"

hist.add("D6*D10",frequencies)
hist.render_to_file('dice_visual.svg')
