"""
Sample test case
"""
from django.test import SimpleTestCase
from . import calc


class CalcTests(SimpleTestCase):
    """
    Test the calc module
    """

    def test_add_numbers(self):
        """
        Test adding numbers
        """
        result = calc.add(5, 10)
        self.assertEqual(result, 15)

    def test_substract_numbers(self):
        """
        Test substracting numbers
        """
        result = calc.substract(10, 15)
        self.assertEqual(result, 5)
