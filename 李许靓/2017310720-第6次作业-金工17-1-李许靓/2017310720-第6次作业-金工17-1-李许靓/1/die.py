from random import randint
import pygal

class Die():
    def __init__(self,sides=6):
        self.sides=sides
    def roll(self):
        return randint(1,self.sides)


# Create two D6 dice.
die1=Die()
die2=Die(10)

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die1.roll() * die2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die1.sides * die2.sides
for value in range(1, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling D6 and D10 dice 1000 times."
hist.x_labels = list(range(1,max_result))
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 * D10', frequencies)
hist.render_to_file('dice_visual.svg')
