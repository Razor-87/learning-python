# 16.09.2017
import pygal

from random_walk import RandomWalk

# Keeping making new walks, as long as the program active.
while True:
    # Make a random walk, and plot the points.
    rw = RandomWalk()

    xy_chart = pygal.XY(stroke=False)
    xy_chart.title = 'Random Walk'
    xy_chart.add('RW', rw.fill_walk())
    xy_chart.show_legend = False
    xy_chart.show_x_labels = False
    xy_chart.show_y_labels = False
    xy_chart.show_x_guides = False
    xy_chart.show_y_guides = False
    xy_chart.dots_size = 1
    xy_chart.render_to_file('rw_visual.svg')

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
