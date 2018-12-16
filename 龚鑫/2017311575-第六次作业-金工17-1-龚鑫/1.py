import pygal
from random import randint
class Die():
    """A class representing a single die."""
    def __init__(self,num_sides=6):
        """Assume a six-sided die."""
        self.num_sides=num_sides

    def roll(self):
        """Return a random value between 1 and number of sides."""
        return randint(1,self.num_sides)
#create a D6 dice and a D10 dice.
die_1=Die()
die_2=Die(10)
#Make some rolls,and store results in a list.
results=[]
for roll_num in range(1000):
    result=die_1.roll()*die_2.roll()
    results.append(result)
#Analyze the results.
frequencies=[]
max_result=die_1.num_sides*die_2.num_sides
for value in range(1,max_result+1):
    frequency=results.count(value)
    frequencies.append(frequency)
#Visualize the results.
hist=pygal.Bar()
hist.title="Results of rolling D6 and D10 dice 1000 times. "
hist.x_labels=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60']
hist.x_title="Result"#设置x轴标题
hist.y_title="Frequency of Result"#设置y轴标题

hist.add('D6+D10',frequencies)#传入数据及标签
hist.render_to_file('dice_visual.svg')#保存图片
