import pygal
from die import Die
# Create two D6 dice.
die_1 = Die()
die_2 = Die(10)
# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die_1.roll() * die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides * die_2.num_sides

for value in range(1, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling two D6 dice 1000 times."
hist.x_labels = []
for i in range(1, max_result+1):
    i=str(i)
    hist.x_labels.append(i)
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 * D10', frequencies)
hist.render_to_file('dice_visual_two_dice_6_10.svg')
