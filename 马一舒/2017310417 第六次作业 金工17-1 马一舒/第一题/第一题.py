import pygal
from random import randint
class Die():
    """创建一个骰子类"""
    def __init__(self,sides):
        """初始化面数属性"""
        self.sides=sides
    def roll_die(self):
        """产生位于1到骰子面数之间的随机数"""
        return randint(1,self.sides)

Digits=[]
for roll_num in range(100):
    sz6=Die(6)
    """先掷6面骰子"""
    digit1=sz6.roll_die()
    sz10=Die(10)
    """先掷10骰子"""
    digit2=sz10.roll_die()
    digits=digit1*digit2
    Digits.append(digits)

frequencies=[]
max_result = sz6.sides * sz10.sides
for value in range(1,max_result+1):
    frequency = Digits.count(value)
    frequencies.append(frequency)
#Visualize the results.
hist=pygal.Bar()
hist.title="Result of rolling a D6 and a D10 100 times"
hist.x_labels =['1','2','3','4','5','6','7','8','9','10','12','14','15','16','18','20','21','24','25','27','28','30','32','35','36','40','42','45','48','49','50','54','56','60']
hist.x_title="Digits"
hist.y_title="Frequency of Resullt"
hist.add('D6*D10',frequencies)
hist.render_to_file('dice_visual_two_die_6_10.svg')
