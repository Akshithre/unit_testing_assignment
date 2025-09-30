import unittest

def divide(a, b):
    return a / b

class TestDivision(unittest.TestCase):
    def test_valid_division(self):
        self.assertAlmostEqual(divide(10, 2), 5.0)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

if __name__ == "__main__":
    unittest.main()
