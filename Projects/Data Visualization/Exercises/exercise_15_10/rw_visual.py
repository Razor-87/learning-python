# 15.09.2017
import pygal

from random_walk import RandomWalk

# Keeping making new walks, as long as the program active.
while True:
    # Make a random walk, and plot the points.
    rw = RandomWalk()
    rw.fill_walk()

    # Set the size of the plotting window.
    # plt.figure(dpi=128, figsize=(10, 6))

    xy_chart = pygal.XY(stroke=False)
    xy_chart.title = 'Random Walk'

    # line_chart.x_labels = list(range(rw.num_points))
    xy_chart.add('RW', [rw.xy_values])
    # plt.plot(rw.x_values, rw.y_values, linewidth=1)

    # # Remove the axes.
    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)

    xy_chart.render()

    # keep_running = input("Make another walk? (y/n): ")
    # if keep_running == 'n':
    #     break
