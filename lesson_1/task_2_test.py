import unittest
from task_2 import *


class IsPrimeTest(unittest.TestCase):
    def test_is_prime(self):
        self.assertEqual(is_prime(9), False)
        self.assertEqual(is_prime(3), True)
        self.assertEqual(is_prime(17), True)


if __name__ == "__main__":
    unittest.main()
