import pygal

from die import Die

#创建一个D6和D10
die_1=Die()
die_2=Die(10)

#掷骰子多次，并将结果存储在一个列表中
results=[]
for roll_num in range(1000):
    result=die_1.roll()*die_2.roll()
    results.append(result)

#分析结果
frequencies=[]
max_result=die_1.num_sides*die_2.num_sides
for value in range(1,max_result+1):
    frequency=results.count(value)
    frequencies.append(frequency)
print(frequencies)

#可视化结果
hist=pygal.Bar()

hist.title="Results of rolling two D6 1000 times."
hist.x_labels=[]
for num in range(1,max_result+1):
    hist.x_labels.append(num)
hist.x_title="Result"
hist.y_title="Frequency of Result"

hist.add('D6*D6',frequencies)
hist.render_to_file('dice_visual.svg')
