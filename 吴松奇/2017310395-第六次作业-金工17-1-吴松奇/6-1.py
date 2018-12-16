import pygal
from random import randint
class die():
    def __init__(self,sides=6):
        self.sides=sides
    def roll_die(self):
        return randint(1,self.sides)
#创建一个六面的骰子和一个十面的骰子
die_1=die()
die_2=die(10)
#掷骰子并将结果储存在列表里
results=[]
for roll_num in range(500000):
    result=die_1.roll_die()*die_2.roll_die()
    results.append(result)
#分析结果
x=[]
frequencies=[]
max_result=die_1.sides*die_2.sides
for value in range(1,max_result+1):
    if value in results:
        x.append(value)
    if results.count(value):
        frequency=results.count(value)
        frequencies.append(frequency)
#可视化结果
hist=pygal.Bar()
hist.title="掷500000次六面和十面的骰子，并将点数相乘的结果"
hist.x_title="结果"
hist.y_title="频率"
hist.x_labels=x
hist.add("D6*D10",frequencies)
hist.render_to_file("dice_visual.svg")
