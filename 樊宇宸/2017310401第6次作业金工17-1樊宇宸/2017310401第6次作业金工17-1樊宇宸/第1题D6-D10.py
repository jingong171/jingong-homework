import pygal
from die import Die
#创建一个D6，一个D10
die1=Die()
die2=Die(10)
#掷几次骰子，并将结果存储在results中
results=[]
for roll_num in range(1000):
    """连续掷100次骰子"""
    #将两个骰子结果乘积作为结果
    result=die1.roll()*die2.roll()
    results.append(result)
#分析结果将每个结果出现次数记录在列表frequencies中
frequencies=[]
#可能结果的最大值是两骰子面数乘积
max_result=die1.num_sides*die2.num_sides
for value in range(1,max_result+1):
    """记录每个可能结果1到max_result中出现的频数"""
    frequency=results.count(value)
    frequencies.append(frequency)
#创建柱状图
hist=pygal.Bar()
#设置标题和x,y轴属性
hist.titile="掷6面和10面骰子1000次结果的乘积"
hist.x_labels=[str(x) for x in range(1,61)]
hist.x_title="结果"
hist.y_title="频数"
hist.add('D6*D10',frequencies)
hist.render_to_file('dice_visual.svg')
