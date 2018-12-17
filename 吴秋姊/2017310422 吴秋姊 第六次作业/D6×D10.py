import pygal
from die import Die
# Create one D6 and one D10 dice.
die_1 = Die(6)
die_2 = Die(10)
# Make some rolls, and store results in a list.
results = []
for roll_num in range(30000):
    result = die_1.roll() * die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides * die_2.num_sides

for value in range(1,max_result+1):
    if results.count(value):
        frequency = results.count(value)
        frequencies.append(frequency)

# Store every possible result in the list.
possible_value=[]
for value in range(1,max_result+1):
    if value in results:
        possible_value.append(value)
        
# Visualize the results.
hist = pygal.Bar()
hist.title = "Results of rolling D6 and D10 dice 30000 times."
hist.x_labels = possible_value
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 × D10', frequencies)
hist.render_to_file('multiply_visual.svg')

