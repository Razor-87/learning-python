# 14.08.2017
import unittest
from exercise_test_class import Employee


class TestEmployee(unittest.TestCase):
    """Tests for the class Employee"""

    def setUp(self):
        """Creates a test dataset."""
        self.employee_test = Employee('sergey', 'razor', 70000)

    def test_give_default_raise(self):
        """Checks function with default value"""
        self.employee_test.give_raise()
        self.assertEqual(75000, self.employee_test.salary)

    def test_give_custom_raise(self):
        """Checks function with custom value"""
        self.employee_test.give_raise(7777)
        self.assertEqual(77777, self.employee_test.salary)


unittest.main()
