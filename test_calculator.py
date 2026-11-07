import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:

    def test_add_negative(self):
        self.assertEqual(self.calc.add(-4, 2), -2)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(6, 2), 4)
        self.assertEqual(self.calc.subtract(2, 6), -4)

    def test_subtract_negative(self):
        self.assertEqual(self.calc.subtract(6, -2), 8)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 7), 14)

    def test_multiply_negative(self):
        self.assertEqual(self.calc.multiply(2, -9), -18)
        self.assertEqual(self.calc.multiply(-2, 9), -18)
        self.assertEqual(self.calc.multiply(-2, -9), 18)

    def test_divide(self):
        self.assertEqual(self.calc.divide(9, 3), 3)
        self.assertEqual(self.calc.divide(9, 0), "Can not divie!!")

    def test_divide_negative(self):
        self.assertEqual(self.calc.divide(-12, 4), -3)
        self.assertEqual(self.calc.divide(4, -12), 0)
        self.assertEqual(self.calc.divide(-12, -4), 3)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(5, 2), 1)
        self.assertEqual(self.calc.modulo(10, 3), 1)
        self.assertEqual(self.calc.modulo(9, 3), 0)
        self.assertEqual(self.calc.modulo(7, 0), "Can not modulo")

    def test_modulo_negative(self):
        self.assertEqual(self.calc.modulo(-10, 3), -1)
        self.assertEqual(self.calc.modulo(-9, 3), 0)
        self.assertEqual(self.calc.modulo(-10, -3), -1)
        

if __name__ == '__main__':
    unittest.main()