# 12.09.2017
from die import Die

import pygal

# Create two D6 dice.
die_1 = Die()
die_2 = Die()

# Make same rolls, and store results in a list.
results = [die_1.roll() * die_2.roll() for roll_num in range(50000)]

# Analyze the results.
max_result = die_1.num_sides * die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling two D6 dice 50000 times."
hist.x_labels = [str(num) for num in range(2, 37)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 * D6', frequencies)
hist.render_to_file('dice_visual.svg')
