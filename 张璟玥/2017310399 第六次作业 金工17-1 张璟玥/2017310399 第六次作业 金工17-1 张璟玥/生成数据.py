from die import Die
import pygal
#创建两个骰子
die_1=Die(6)
die_2=Die(10)
results=[]
for roll_num in range(1000):
    result =die_1.roll()*die_2.roll()
    results.append(result)
    

#计算各可能结果出现的次数
frequencies=[]
max_result=die_1.num_sides*die_2.num_sides
for value in range(1,max_result+1):
    frequency=results.count(value)
    frequencies.append(frequency)
#绘制图标
hist=pygal.Bar()
hist._title="Resluts of rolling a D6 and a D10 50000 times."
hist.x_labels=results
hist.x_title="Result"
hist._y_title="Frequency of Result"
hist.add('D6*D10',frequencies)
hist.render_to_file('dice_visual.svg')