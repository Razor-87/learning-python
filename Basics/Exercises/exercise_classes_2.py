# 30.07.2017
class Restaurant():
    """A simple restaurant model."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant_name and cuisine_type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Displays information about the restaurant"""
        print("\nThe restaurant is called: " + self.restaurant_name.title())
        print("His national cuisine: " + self.cuisine_type.title())


restaurant_tasty = Restaurant('tasty food', 'italian')
restaurant_pier = Restaurant('pier', 'mediterranean')
restaurant_peking = Restaurant('peking', 'chinese')


restaurant_tasty.describe_restaurant()
restaurant_pier.describe_restaurant()
restaurant_peking.describe_restaurant()
