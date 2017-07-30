# 30.07.2017
class User():
    """Simple user model."""

    def __init__(self, first_name, last_name, age, city):
        """User information."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city

    def describe_user(self):
        """Displays the user description."""
        print("\nFull user name: " + self.first_name.title() + " " +
              self.last_name.title() + ".")
        print("Age of the user: " + str(self.age) + ".")
        print("The user lives in " + self.city.title() + ".")

    def greet_user(self):
        """Prints a greeting to the user."""
        print("\nHello, " + self.first_name.title() + " " +
              self.last_name.title() + ".")


user_1 = User('john', 'smit', 33, 'nashville')
user_2 = User('lena', 'lee', 41, 'livonia')
user_3 = User('mary', 'russo', 31, 'jackson')


user_1.describe_user()
user_2.describe_user()
user_3.describe_user()

user_1.greet_user()
user_2.greet_user()
user_3.greet_user()
