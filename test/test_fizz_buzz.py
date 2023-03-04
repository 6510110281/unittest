from coe_number.FizzBuzz import fizz_buzz

import unittest


class TestFizzBuzz(unittest.TestCase):
    def test_3_in_FizzBuzz(self):
        test_input = 3
        self.assertEqual(fizz_buzz(test_input), 'Fizz')

    def test_6_in_FizzBuzz(self):
        test_input = 6
        self.assertEqual(fizz_buzz(test_input), 'Fizz')

    def test_5_in_FizzBuzz(self):
        test_input = 5
        self.assertEqual(fizz_buzz(test_input), 'Buzz')

    def test_10_in_FizzBuzz(self):
        test_input = 10
        self.assertEqual(fizz_buzz(test_input), 'Buzz')

    def test_15_in_FizzBuzz(self):
        test_input = 15
        self.assertEqual(fizz_buzz(test_input), 'FizzBuzz')
