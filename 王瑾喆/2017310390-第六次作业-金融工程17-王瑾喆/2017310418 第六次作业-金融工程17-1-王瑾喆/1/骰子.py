#导入库
from random import randint
import pygal

#声明类
class Die():
    """创建骰子类"""

    def __init__(self,side_num=6):
        """初始化骰子的属性"""
        self.side_num=side_num

    def roll(self):
        """定义掷骰子的函数,随机产生一个代表骰子面的值"""
        return randint(1,self.side_num)

#创建6面和10面的骰子实例
die1=Die()
die2=Die(10)

#创建列表来储存结果
results=[]

for i in range(1,501):
    result1=die1.roll()
    result2=die2.roll()
    results.append(result1*result2)


frequencies=[]
for value in range(1,die1.side_num*die2.side_num+1):
    frequency=results.count(value)
    frequencies.append(frequency)

#对结果进行可视化处理
hist=pygal.Bar()
#设置图表属性
hist.title="掷10面和6面骰子相乘的结果"
hist.x_labels=[i for i in range(1,61)]
hist.x_title="相乘后的结果"
hist.y_title="结果的次数"
#设置标签
hist.add('D6*D10',frequencies)
#存储结果
hist.render_to_file('结果.svg')


    

