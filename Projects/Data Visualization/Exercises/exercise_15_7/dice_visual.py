# 12.09.2017
from die import Die

import pygal

# Create two D8 dice.
die_1 = Die()
die_2 = Die()

# Make same rolls, and store results in a list.
results = [die_1.roll() + die_2.roll() for roll_num in range(500000)]

# Analyze the results.
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling two D8 dice 500000 times."
hist.x_labels = [str(num) for num in range(2, 17)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D8 + D8', frequencies)
hist.render_to_file('dice_visual.svg')
