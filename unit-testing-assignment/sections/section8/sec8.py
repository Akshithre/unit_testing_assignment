import unittest

class Calculator:
    def add(self, x, y): return x + y
    def sub(self, x, y): return x - y
    def mul(self, x, y): return x * y
    def div(self, x, y):
        if y == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return x / y

class TestCalculator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(5, 7), 12)

    def test_sub(self):
        self.assertEqual(self.calc.sub(10, 3), 7)

    def test_mul(self):
        self.assertEqual(self.calc.mul(4, 6), 24)

    def test_div(self):
        self.assertEqual(self.calc.div(20, 5), 4.0)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.div(5, 0)

    @classmethod
    def tearDownClass(cls):
        cls.calc = None

if __name__ == "__main__":
    unittest.main()
