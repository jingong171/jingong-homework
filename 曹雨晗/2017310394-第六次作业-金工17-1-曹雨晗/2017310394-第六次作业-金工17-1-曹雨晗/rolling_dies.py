import pygal

from die import Die

die1 = Die()
#创建一个默认六面的骰子
die2 = Die(10)
#创建一个十面的骰子


results = []
#创建一个空列表来储存两个骰子投掷出的数值的乘积
for roll_num in range(1000):
    result = die1.roll() * die2.roll()
    results.append(result)


frequencies = []
#创建一个空列表来储存取得各个可能值的次数
max_result = die1.num_sides * die2.num_sides
for value in range(1, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)


#可视化结果
hist = pygal.Bar()
hist.title = "Results of rolling a D6 and a D10 1000 times."
hist.x_labels = list(range(1, max_result+1))
hist.x_title = "Result"
hist.y_title = "Frequency of result"
hist.add('D6 * D10', frequencies)
hist.render_to_file('rolling_two_diffierent_dies.svg')
