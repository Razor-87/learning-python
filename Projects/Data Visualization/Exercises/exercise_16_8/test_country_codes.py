# 21.09.2017
import unittest
from country_codes import get_country_code


class CountryCodesTest(unittest.TestCase):
    """Tests for the function get_country_code()"""

    def setUp(self):
        """Creates a test dataset."""
        self.countries = ['Russian Federation', 'Japan', 'Bolivia', 'Vietnam']
        self.codes = ['ru', 'jp', 'bo', 'vn']
        self.result = []

    def test_country_codes(self):
        """Verify that the function call is correct."""
        while self.countries:
            self.country = self.countries.pop(0)
            self.result.append(get_country_code(self.country))
        self.assertEqual(self.result, self.codes)


unittest.main()
