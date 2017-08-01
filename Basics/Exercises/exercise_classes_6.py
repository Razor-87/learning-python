# 01.08.2017
class Restaurant():
    """A simple restaurant model."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant_name and cuisine_type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Displays information about the restaurant"""
        print("The restaurant is called: " + self.restaurant_name.title())
        print("His national cuisine: " + self.cuisine_type.title())

    def open_restaurant(self):
        """Displays a message stating that the restaurant is open."""
        print("\nNow the restaurant is open!")


class IceCreamStand(Restaurant):
    """A simple ice cream stand model"""

    def __init__(self, flavors, restaurant_name='', cuisine_type=''):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        """Display of ice cream flavors"""
        print("Now available ice cream:")
        for flavor in self.flavors:
            print("- " + flavor.title())


my_flavors = ['strawberry', 'chocolate', 'orange']
my_icecream_stand = IceCreamStand(my_flavors)
my_icecream_stand.display_flavors()
