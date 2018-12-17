# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 08:50:24 2018

@author: WSQ
"""

from random import randint
class Die():
    def _init_(self,sides=6):
        self.sides=sides
    def roll_die(self):
        return randint(1,self.sides)
import pygal
die_1=Die()
die_2=Die(10)
results=[]
times=int(input("请输入您想投骰子的次数："))
for i in range(times+1):
    """投骰子并记录结果"""
    result=die_1.roll_dies()*die_2.roll_dies()
    results.append(result)

values=[]
frequencies=[]
for value in range(1,time+1):
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

