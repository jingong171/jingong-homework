import pygal
from random import randint

class Die():
    """表示一个骰子的类"""
    
    def __init__(self,num_sides=6):
        """骰子默认6面"""
        self.num_sides=num_sides

    def roll(self):
        return randint(1,self.num_sides)

die1=Die(6)
die2=Die(10)

#同时掷两个骰子，乘积结果存储在results列表中
results=[]
for roll_num in range(10000):
    result=die1.roll()*die2.roll()
    results.append(result)

#获得两个骰子乘积的所有可能结果，存储在x_labels列表中
x_labels=[]
for i in range(1,7):
    for j in range(1,11):
        product=i*j
        if product in x_labels:
            continue
        else:
            x_labels.append(product)
x_labels.sort() #按递增顺序排列，作为可视化时的横坐标
            
#分析结果
frequencies=[]
for value in x_labels:
    frequency=results.count(value)
    frequencies.append(frequency)

#对结果进行可视化
hist=pygal.Bar()

hist.title="Result of rolling a D6 dice and a D10 dice 10000 times"
hist.x_labels=x_labels
hist.x_title="Result"
hist.y_title="Frequency of Result"

hist.add("D6*D10",frequencies)
hist.render_to_file('Die_Visual.svg')
