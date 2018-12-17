from dices import dices
import pygal
'''创建两个骰子
    分别为6面和10面'''
dices_1=dices()
dices_2=dices(10)
results=[]
'''设定好掷骰子次数为10000次'''
for roll_number in range(10000):
    result=dices_1.roll()*dices_2.roll()
    results.append(result)
frequencies=[]
#统计每个结果出现的频率
for value in range(1,dices_1.sides*dices_2.sides):
    frequency=results.count(value)
    frequencies.append(frequency)
#可视化所得到的结果
hist=pygal.Bar()
hist.title="Results of rolling one D6 and one D10 and compute their multiple for 10000 times"
hist.x_lables=results
hist.x_title="Results"
hist.y_title="Frequencies"
hist.add('D6*D10',frequencies)
hist.render_to_file('dice_visual.svg')
