
from die import Die

import pygal

 

#创建两个点数不同的骰子

die_1=Die()

die_2=Die(10)

 

#投掷多次并将相乘结果记录在列表中

results=[]

 

for roll_num in range(50000):

    result=die_1.roll() * die_2.roll()

    results.append(result)

 

#统计频率

frequencies=[]

max_result=die_1.num_sides * die_2.num_sides

for value in range(1,max_result+1):

    if results.count(value):

       frequency=results.count(value)

       frequencies.append(frequency)

 

#可视化结果

#将所有可能的乘积保存在列表xs中，所得乘积并不连续

xs=[]

for value in range(1,max_result+1):

    if value in results:

       xs.append(value)

hist=pygal.Bar()

hist.title = "Results of rolling a D6 and a D10 50,000 times." 

hist.x_labels=xs

hist.x_title = "Result" 

hist.y_title = "Frequency of Result" 

 

hist.add('D6 * D10', frequencies) 

hist.render_to_file('multiply_visual.svg') 

