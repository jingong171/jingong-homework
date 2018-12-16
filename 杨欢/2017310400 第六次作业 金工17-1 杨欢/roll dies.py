from die import Die
import pygal

#创建两个骰子
die6=Die()
die10=Die(10)
#results用于存储所有可能的结果
results=[]

times=int(input("请输入您想投骰子的次数："))
for i in range(times+1):
    """投骰子并记录结果"""
    d6=die6.roll_dies()
    d10=die10.roll_dies()
    result=d6*d10
    results.append(result)

values=[]
frequencies=[]
for value in range(1,61):
    """对于在结果内的数字，数出其发生的次数"""
    if value in results:
        values.append(value)
        frequency=results.count(value)
        frequencies.append(frequency)

#画出直方图并保存
hist=pygal.Bar()
hist.title="10面的骰子与6面的骰子的点数相乘分布图"
hist.x_title="点数乘积"
hist.x_labels=values
hist.y_title="频数"
hist.add('D6*D10',frequencies)
hist.render_to_file('d6_d10.svg')

