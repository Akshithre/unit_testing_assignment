
import unittest
from code.mycal import Calculations

class TestCalculations(unittest.TestCase):

    def test_sum(self):
        calculation = Calculations(8, 2)
        # Intentionally setting the expected value to 11 to demonstrate a failing test
        self.assertEqual(calculation.get_sum(), 11, 'The sum is wrong.')

if __name__ == '__main__':
    unittest.main()