from random import randint

#首先创建一个骰子类
class Die():
    
    def __init__(self,num_sides=6):
        "默认设置为一般的六面骰子"
        self.num_sides = num_sides

    def roll(self):
        "返回一个骰子数字范围内的值"
        return randint(1,self.num_sides)

#创立6面和10面的实例
die_1 = Die(6)
die_2 = Die(10)

#得出实例的值相乘的结果
results = []
for roll_num in range(20):
    result = die_1.roll()*die_2.roll()
    results.append(result)

#进行可视化
import matplotlib.pyplot as plt

x_values = list(range(1,21))
y_values = results
plt.scatter(x_values,y_values, edgecolor='red', s = 40)
plt.title("Dice roll experiment",fontsize = 24)
plt.xlabel("The N roll of dice",fontsize = 14)
plt.ylabel("Throw value multiplied by result",fontsize = 14)
plt.tick_params(axis = 'both',which = 'major', labelsize = 14)
plt.show()
