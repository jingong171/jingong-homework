import pygal
import random
class Die():
    def __init__(self,side_num):
        self.side_num=side_num
    def roll(self):
        result=random.randint(1,self.side_num)
        return result
d6=Die(6)
d10=Die(10)
result=[]
for i in range(1,10000):
    result.append(d6.roll()*d10.roll())
result1=list(set(sorted(result)))
x_la=list(map(str,result))
frequency=[]
for i in result1:
    frequency.append(x_la.count(str(i)))
hist=pygal.Bar()
hist.title='Result of frequency'
hist.width=1500
hist.x_title='result'
hist.y_title='frequency'
hist.x_labels=result1
hist.add('Frequency',frequency)
hist.render_to_file('frequency.svg')