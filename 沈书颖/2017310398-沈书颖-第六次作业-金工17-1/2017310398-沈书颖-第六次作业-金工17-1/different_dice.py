from die import Die
import pygal

#创建一个六面和十面的骰子
die_1=Die()
die_2=Die(10)

#掷骰子多次，并将结果写在一个列表里
results=[]
for roll_num in range(50000):
    result=die_1.roll()*die_2.roll()
    results.append(result)

#分析结果
frequencies=[]
max_result=die_1.sides*die_2.sides
for value in range(1,max_result+1):
    frequency=results.count(value)
    frequencies.append(frequency)
    
hist=pygal.Bar()
hist,title="Results of rolling a D6 and a D10 50000 times"
hist.x_labels=[range(1,max_result+1)]
hist.x_title="result"
hist.y_title="frequency of result"

hist.add('D6+D10',frequencies)
hist.render_to_file('dice_visual.svg')
