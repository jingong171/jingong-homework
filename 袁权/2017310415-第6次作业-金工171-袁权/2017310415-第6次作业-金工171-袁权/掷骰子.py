#先创建一个骰子类
from random import randint
class Die():
    """A class representing a single die."""

    def __init__(self,num_sides=6):
        """Assume a six-side die"""
        self.num_sides=num_sides

    def roll(self):
        """"Return a random value between 1 and number of sides."""
        return randint(1,self.num_sides)


import pygal
#创建骰子对象
die_1=Die()
die_2=Die(10)
results=[]
for roll_num in range(1000):
    result=die_1.roll()*die_2.roll()
    results.append(result)


#分析结果
frequencies = []
max_result = die_1.num_sides * die_2.num_sides
for value in range(1, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#Visualize the  results
hist=pygal.Bar()

hist.title="分别抛一个六面的和十面的骰子的点数之积"
List=[]
for i in range(1,61):
    List.append(i)
hist.x_labels=List
hist.x_title="Result"
hist.y_title="Frequency of Result"

hist.add("点积",frequencies)
hist.render_to_file('die_visual.svg')
