from coe_number.Caesar_Cipher import caesarCipher

import unittest

class TestCaesarCipher(unittest.TestCase):
    def test_abcdefghijklmnopqrstuvwxyz_and_2_in_caesarcipher(self):
        x = 'abcdefghijklmnopqrstuvwxyz'
        result = caesarCipher(x,2)
        self.assertEqual(result,'cdefghijklmnopqrstuvwxyzab')
    def test_abcdefghijklmnopqrstuvwxyz_and_0_caesarcipher(self):
        x = 'abcdefghijklmnopqrstuvwxyz'
        result = caesarCipher(x,0)
        self.assertEqual(result,'abcdefghijklmnopqrstuvwxyz')
    def test_abcdefghijklmnopqrstuvwxyz_and_minus2_in_caesarcipher(self):
        x = 'abcdefghijklmnopqrstuvwxyz'
        result = caesarCipher(x,-2)
        self.assertEqual(result,'yzabcdefghijklmnopqrstuvwx')
    def test_Secret_Word_and_0_in_caesarcipher(self):
        x = 'Secret Word'
        result = caesarCipher(x,0)
        self.assertEqual(result,'Secret Word')
    def test_Secret_Word_and_2_in_caesarcipher(self):
        x = 'Secret Word'
        result = caesarCipher(x,5)
        self.assertEqual(result,'Xjhwjy Btwi')
