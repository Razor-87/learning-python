# 14.08.2017
class Employee():
    """Class describing the employee."""

    def __init__(self, first, last, salary):
        """Initialization of employee attributes."""
        self.first = first
        self.last = last
        self.salary = salary

    def show_info(self):
        """Displays information about the employee."""
        full_name = self.first.title() + ' ' + self.last.title()
        print("\nFull name: " + full_name + ".")
        print("Annual salary: $" + str(self.salary) + ".")

    def give_raise(self, salary_up=5000):
        """Increases the annual salary of an employee."""
        self.salary_up = salary_up
        if salary_up != 5000:
            self.salary += salary_up
        else:
            self.salary += 5000
        return self.salary
