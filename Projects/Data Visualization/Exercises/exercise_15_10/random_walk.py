# 15.09.2017
from random import choice


class RandomWalk():
    """A class to generate random walks."""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points

        # All walks start at (0, 0).
        self.x_values = 0
        self.y_values = 0

    def fill_walk(self):
        """Calculate all the points in the walk."""

        # Keep taking steps until the walk reaches the desired length.
        self.times = 0
        while self.times < self.num_points:
            # Decide which direction to go
            #  and how far to go in that direction.
            self.times += 1
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the next x and y values.
            next_x = self.x_values + x_step
            next_y = self.y_values + y_step

            self.x_values = next_x
            self.y_values = next_y
            self.xy_values = (self.x_values, self.y_values)
