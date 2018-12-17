from random import randint
import pygal
class Die:
    def __init__(self, num_sides=6):
        self.num_sides = num_sides
    def roll(self):
        return randint(1, self.num_sides)
die1 = Die()
die2 = Die(10)
results = []
for roll_num in range(1000):
    result1 = die1.roll()
    int(result1)
    result2 = die2.roll()
    int(result2)
    results.append(result1*result2)
frequencies = []
for value in range(1, 61):
    frequency = results.count(value)
    frequencies.append(frequency)
hist = pygal.Bar()
hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = []
for i in range(1, 61):
    hist.x_labels.append(i)
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6*D10', frequencies)
hist.render_to_file('die_visual.svg')
