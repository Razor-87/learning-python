# 31.07.2017
class User():
    """Simple user model."""

    def __init__(self, first_name, last_name, age, city):
        """User information."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.login_attempts = 0

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

    def increment_login_attempts(self):
        """Increases the value 'login_attempts' by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets the value 'login_attempts'."""
        self.login_attempts = 0


user = User('john', 'smit', 33, 'nashville')
print(user.login_attempts)

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(user.login_attempts)

user.reset_login_attempts()
print(user.login_attempts)
