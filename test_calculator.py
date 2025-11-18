# https://github.com/hatchkor/lab11-RH-YH.git
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    def test_add(self): # 3 assertions
        self.assertEqual(add(2,3), 5)
        self.assertEqual(add(50,20), 70)
        self.assertEqual(add(103, 292), 395)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(5,2), 3)
        self.assertEqual(subtract(3,5), -2)
        self.assertEqual(subtract(100, 25), 75)

    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(3,2), 6)
        self.assertEqual(mul(-2,10), -20)
        self.assertEqual(mul(-6,-9), 54)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(2,6), 3)
        self.assertEqual(div(5,100), 20)
        self.assertEqual(div(-25, 25), -1)

    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0,5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(5,25),2)
        self.assertEqual(logarithm(5,9765625), 10)
        self.assertEqual(logarithm(2, 8), 3)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0,5)


    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(5,0)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3,4), 5)
        self.assertEqual(hypotenuse(7,24),25)
        self.assertEqual(hypotenuse(12,5),13)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-1)
        self.assertEqual(square_root(36), 6)
        self.assertEqual(square_root(25), 5)

# Do not touch this
if __name__ == "__main__":
    unittest.main()