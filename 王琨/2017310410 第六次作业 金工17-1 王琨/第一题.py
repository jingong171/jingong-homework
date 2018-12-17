from random import randint
import pygal
class Die():
    def __init__(self,num_sides=6):
        self.num_sides=num_sides
    def roll(self):
        return randint(1,self.num_sides)


die1=Die(6)
die2=Die(10)

results=[]
for i in range(1000):
    result=die1.roll()*die2.roll()
    results.append(result)

frequencies=[]
for value in range(1,61):
    frequency=results.count(value)
    frequencies.append(frequency)

hist=pygal.Bar()
hist.title='Result of multiplying the points of two dies'
hist.x_labels=['1','2','3','4','5','6','7','8','9','10','12','14','15','16','18','20','21','24','25','27','28','30','32','35','36','40','42','45','48','50','54','60']
hist.x_title='Result'
hist.y_title='Frequency of result'
hist.add('MULTIPLY',frequencies)
hist.render_to_file('第一题.svg')
