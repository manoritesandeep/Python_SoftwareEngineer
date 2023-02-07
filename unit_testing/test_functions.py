from unittest import TestCase
from functions import divide, multiply


class TestFunctions(TestCase):
    def test_divide_result(self):
        dividend = 15
        divisor = 3
        expected_result = 5.0
        self.assertAlmostEqual(divide(dividend, divisor), expected_result, delta=0.00001)

    def test_divide_negative(self):
        dividend = 15
        divisor = -3
        expected_result = -5.0
        self.assertAlmostEqual(divide(dividend, divisor), expected_result, delta=0.0001)

    def test_divide_dividend_zero(self):
        dividend = 0
        divisor = -3
        expected_result = 0
        self.assertEqual(divide(dividend, divisor), expected_result)

    def test_divide_error_on_zero(self):
        with self.assertRaises(ValueError):
            divide(25, 0)
        # OR
        # self.assertRaises(ValueError, lambda: divide(25, 0))

    def test_multiply_error(self):
        with self.assertRaises(ValueError):
            multiply()

    def test_multiply_single_value(self):
        expected = 15
        self.assertEqual(multiply(expected), expected)

    def test_multiply_zero(self):
        expected = 0
        self.assertEqual(multiply(expected), expected)

    def test_multiply_result(self):
        inputs = (3, 5)
        expected = 15
        self.assertEqual(multiply(*inputs), expected)

    def test_multiply_input_with_zero(self):
        inputs = (3, 5, 0)
        expected = 0
        self.assertEqual(multiply(*inputs), expected)

    def test_multiply_negative(self):
        inputs = (3, -5, 2)
        expected = -30
        self.assertEqual(multiply(*inputs), expected)

    def test_multiply_floats(self):
        inputs = (3.0, 5)
        expected = 15.0
        self.assertEqual(multiply(*inputs), expected)


