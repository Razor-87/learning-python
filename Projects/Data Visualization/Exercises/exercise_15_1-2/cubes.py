# 19.08.2017
import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.plasma,
            edgecolor='none', s=20)

# Set chart title and label axes.
plt.title("Cube Numbers", fontsize=20)
plt.xlabel("Value", fontsize=12)
plt.ylabel("Cube of Value", fontsize=12)

# Set size of tick labels.
plt.tick_params(axis='both', which='major', labelsize=12)

# Set the range for each axis.
plt.axis([0, 5100, 0, 130000000000])

plt.show()
