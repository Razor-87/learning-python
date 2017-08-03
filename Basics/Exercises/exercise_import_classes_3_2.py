# 03.08.2017
from exercise_import_classes_3_1 import User


class Privileges():
    """Administrator privileges."""

    def __init__(self, privileges):
        """Initialize attributes."""
        self.privileges = privileges

    def show_privileges(self):
        """Displays administrator privileges."""
        print("Received privileges:")
        for privilege in self.privileges:
            print("- " + privilege.capitalize())


class Admin(User):
    """Creates an administrator class based on the user class."""

    def __init__(self, privileges, first_name='',
                 last_name='', age='', city=''):
        """Initialize attributes."""
        super().__init__(first_name, last_name, age, city)
        self.privileges = Privileges(privileges)
