from random import randint
class Die():#创建骰子#
    def_init_(self,num_sides=6):#6面骰子#
        self.num_sides=num.sides
    def roll(self):#投掷一个骰子#
        return randint(1,self num_sides)
import pygal
from die import Die
die_1=Die()
die_2=Die(10)#两个骰子6面和10面#
result=[]
for roll_num in range(1000):
    result=die_1.roll()*die_2.roll()
results.append(result)
for value in range(2,max_result+1):
    frequency=results.count(value)
    frequencies.append(frequency)
hist.title="Results of rolling two D6 dice 1000 times."
hist.x_labels=["1","2","3","4","5","6","7","8","9","10","11","12"，"14","15","16"，"18","20","21","24","25","27","28","30","32","35","36","40","42","45","48","50","54","56","60"]
hist.x_title="result"
hist.y_title="frequency of result"
hist.add("D6*D10",frequencies)
hist.render_to_file("dice_visual.svg")
