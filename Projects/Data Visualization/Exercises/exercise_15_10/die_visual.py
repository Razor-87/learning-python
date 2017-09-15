# 14.09.2017
from die import Die

import matplotlib.pyplot as plt

# Create a D6.
die = Die()

# Make some rolls, and store results in a list.
results = [die.roll() for roll_num in range(1000)]

# Analyze the results.
frequencies = [results.count(value) for value in range(1, die.num_sides+1)]

# Visualize the results.
hist = plt.Bar()

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = [str(num) for num in range(1, 7)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
