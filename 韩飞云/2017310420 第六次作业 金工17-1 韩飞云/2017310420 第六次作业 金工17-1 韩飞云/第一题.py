import pygal
from random import randint

#creat a class die
class Die():
    def __init__(self,num_sides=6):
        self.num_sides = num_sides

#creat a number
    def roll (self):
        return randint(1,self.num_sides)

#creat two example
die_1=Die()
die_2=Die(10)

#save result in results
results=[]
for roll_num in range(1000):
    result=die_1.roll()*die_2.roll()
    results.append(result)

#save frequency in frequencies
frequencies=[]

#get max result
max_result=die_1.num_sides*die_2.num_sides

#get frequencies
for value in range(1,max_result+1):
    frequency=results.count(value)
    frequencies.append(frequency)

#paint the result
hist=pygal.Bar()
hist.title="Die6和Die10掷1000次，两值相乘结果"
hist.x_labels=list(range(1,max_result+1))
hist.x_title="Result"
hist.y_title="Frequency of Result"
hist.add('Die6*Die10',frequencies)
hist.render_to_file('the first question.svg')
