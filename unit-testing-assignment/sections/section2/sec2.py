import unittest

def is_even(num):
    return num % 2 == 0

class TestNumberCheck(unittest.TestCase):
    def test_even(self):
        self.assertTrue(is_even(10))
        self.assertFalse(is_even(7))

if __name__ == "__main__":
    unittest.main()
