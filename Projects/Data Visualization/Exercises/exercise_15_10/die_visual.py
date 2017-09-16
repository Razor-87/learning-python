# 16.09.2017
from die import Die

import matplotlib.pyplot as plt

# Create a D6.
die = Die()

# Make some rolls, and store results in a list.
results = [die.roll() for roll_num in range(10000)]

# Analyze the results.
x = range(1, die.num_sides+1)
y = [results.count(value) for value in range(1, die.num_sides+1)]

# Visualize the results.
bar_width = 0.9
plt.bar(x, y, bar_width)
plt.xlabel('Result')
plt.ylabel('Frequency of Result')
plt.title('Results of rolling one D6 1000 times.')
plt.show()
