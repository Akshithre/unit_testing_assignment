import unittest

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def count(self):
        return len(self.items)

class TestCart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()

    def test_add_item(self):
        self.cart.add_item("apple")
        self.assertEqual(self.cart.count(), 1)

    def tearDown(self):
        self.cart = None

if __name__ == "__main__":
    unittest.main()
