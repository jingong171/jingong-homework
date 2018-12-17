from die import Die
import pygal

die1=Die()   #创建一个6面骰子
die2=Die(10)

multiples=[]
for i in range(1,die1.sides+1):
    for j in range(1,die2.sides+1):
        multiple=i*j
        if multiple not in multiples:
            multiples.append(multiple)
multiples.sort()

times=10000      #投骰子的次数
results=[]
for i in range(times):
    result=die1.roll_die()*die2.roll_die()
    results.append(result)

counts=[]
for multiple in multiples:
    count=results.count(multiple)
    counts.append(count)

hist=pygal.Bar()
hist.title="Results of rolling a D6 and a D10 "+str(times)+" times"
hist.x_labels=multiples
hist.x_title="Multiples"
hist.y_title="Frequency of Results"
hist.add(str(times)+" rollings",counts)
hist.render_to_file('dice_visual.svg')
