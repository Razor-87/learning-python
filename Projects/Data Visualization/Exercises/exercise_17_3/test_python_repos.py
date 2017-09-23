# 23.09.2017
import unittest
from python_repos import status_code, total_rep, items_len


class PythonReposTest(unittest.TestCase):
    """Tests for the python_repos"""

    def test_status_code(self):
        """Verify that the function call is correct."""
        self.assertEqual(status_code(), 200)

    def test_total_rep(self):
        """Verify that the function call is correct."""
        self.assertGreater(total_rep(), 1000000)

    def test_items_len(self):
        """Verify that the function call is correct."""
        self.assertEqual(items_len(), 30)


unittest.main()
