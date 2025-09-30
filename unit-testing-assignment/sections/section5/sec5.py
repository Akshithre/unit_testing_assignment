import unittest

def get_username(user_dict):
    return user_dict.get("username")

class TestDictionary(unittest.TestCase):
    def test_existing_key(self):
        user = {"username": "akshith", "age": 23}
        self.assertEqual(get_username(user), "akshith")

    def test_missing_key(self):
        user = {"age": 23}
        self.assertIsNone(get_username(user))

if __name__ == "__main__":
    unittest.main()
