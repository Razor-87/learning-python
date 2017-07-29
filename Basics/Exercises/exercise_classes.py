# 29.07.2017
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


restaurant = Restaurant('tasty food', 'italian')

print("[" + restaurant.restaurant_name.title() + "] " +
      restaurant.cuisine_type.title() + " Cuisine\n")

restaurant.describe_restaurant()
restaurant.open_restaurant()
