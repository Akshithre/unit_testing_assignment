import unittest

def add(a, b):
    return a + b

class TestMathBasics(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add(2, 3), 5)
        self.assertNotEqual(add(1, 1), 3)

if __name__ == "__main__":
    unittest.main()
