import pygal
from die import Die

die1=Die()#创建骰子
die2=Die(10)

multiples=[]#乘积的可能性
for i in range(1,die1.sides+1):
    for j in range(1,die2.sides+1):
        multiple=i*j
        if multiple not in multiples:
            multiples.append(multiple)
multiples.sort()

times=5000#投骰子的次数

results=[]#结果
for i in range(times):
    result=die1.roll()*die2.roll()
    results.append(result)

frequencies=[]#计数
for k in multiples:
    frequency=results.count(k)
    frequencies.append(frequency)

hist=pygal.Bar()#gal

hist.title="Results of D6 Multiples D10 "+str(times)+" times"
hist.x_labels=multiples
hist.x_title="Result of Multiples"
hist.y_title="Frequency of Results"
hist.add(str(times)+" rollings",frequencies)
hist.render_to_file('dice.svg')
