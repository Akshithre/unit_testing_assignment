import unittest

def multiply(a, b):
    return a * b

class TestMultiplication(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_negative_numbers(self):
        self.assertEqual(multiply(-2, 6), -12)

    def test_zero(self):
        self.assertEqual(multiply(5, 0), 0)

if __name__ == "__main__":
    unittest.main()
