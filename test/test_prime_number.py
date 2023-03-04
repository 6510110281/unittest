from coe_number.prime_number import is_prime_list

import unittest


class TestPrimeNumber(unittest.TestCase):
    def test_all_in_list_is_primes(self):
        prime_list = [1, 2, 3]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_one_in_list_is_primes(self):
        prime_list = [4, 5, 6]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

    def test_one_in_list_is_non_primes(self):
        prime_list = [7, 8, 9]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

    def test_all_in_list_is_non_primes(self):
        prime_list = [10, 20, 30]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

    def test_same_in_list_prime(self):
        prime_list = [2, 2, 2]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)
