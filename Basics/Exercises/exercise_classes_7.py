# 02.08.2017
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


class Admin(User):
    """Creates an administrator class based on the user class."""

    def __init__(self, privileges, first_name='',
                 last_name='', age='', city=''):
        """Initialize attributes."""
        super().__init__(first_name, last_name, age, city)
        self.privileges = privileges

    def show_privileges(self):
        """Displays administrator privileges."""
        print("Received privileges:")
        for privilege in self.privileges:
            print("- " + privilege.capitalize())


admin_privileges = ('can add post', 'can delete post', 'can ban user')
admin_1 = Admin(admin_privileges)
admin_1.show_privileges()
