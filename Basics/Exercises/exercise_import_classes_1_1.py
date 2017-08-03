# 03.08.2017
class Restaurant():
    """A simple restaurant model."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant_name and cuisine_type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Displays information about the restaurant"""
        print("\nThe restaurant is called: " + self.restaurant_name.title())
        print("His national cuisine: " + self.cuisine_type.title())

    def set_number_served(self, number):
        """Specifies the number of serviced customers"""
        self.number_served = number

    def increment_number_served(self, increment_number):
        """Specifies the number of serviced customers"""
        self.number_served += increment_number
