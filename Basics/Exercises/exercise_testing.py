# 13.08.2017
import unittest
from exercise_test_function import city_country


class CityCountryTest(unittest.TestCase):
    """Tests for 'exercise_test_function.py'."""

    def test_city_country(self):
        """Verify that the function call is correct."""
        test_cc = city_country('santiago', 'chile')
        self.assertEqual(test_cc, 'Santiago, Chile')

    def test_city_country_population(self):
        """Verify that the function call is correct."""
        test_ccp = city_country('santiago', 'chile', 5000000)
        self.assertEqual(test_ccp, 'Santiago, Chile - population 5000000.')


unittest.main()
