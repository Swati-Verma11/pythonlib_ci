import unittest
# import pytest
from fibonacci.fibonacci import fibonacci


class TestFibo(unittest.TestCase):
    def test_fibonacci_1(self):
        self.assertEqual(fibonacci(1), 1)
    # def test_fibonacci_2(self):
    #     self.assertEqual(fibonacci(2) , 2)


if __name__ == '__main__':
    unittest.main()    