from coe_number.Alternating_Characters import AlternatingCharacter

import unittest

class TestAlternatingCharacter(unittest.TestCase):
    def test_AAAA_in_alternating(self):
        x = 'AAAA'
        result = AlternatingCharacter(x)
        self.assertEqual(result,3)
    def test_BBBBB_in_alternating(self):
        x = 'BBBBB'
        result = AlternatingCharacter(x)
        self.assertEqual(result,4)
    def test_ABABABAB_in_alternating(self):
        x = 'ABABABAB'
        result = AlternatingCharacter(x)
        self.assertEqual(result,0)
    def test_BABABA_in_alternating(self):
        x = 'BABABA'
        result = AlternatingCharacter(x)
        self.assertEqual(result,0)
    def test_AAABBB_in_alternating(self):
        x = 'AAABBB'
        result = AlternatingCharacter(x)
        self.assertEqual(result,4)
        