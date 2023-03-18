import unittest
from divisible_by_x_and_y import is_divisible

class TestDivisible(unittest.TestCase):
    def test_division(self):
        self.assertEqual(is_divisible(6, 2, 4), False)
        self.assertEqual(is_divisible(10, 2, 5), True)

if __name__ == '__main__':
    unittest.main()


