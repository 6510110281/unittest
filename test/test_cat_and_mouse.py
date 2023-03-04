from coe_number.Cat_and_Mouse import cat_and_mouse

import unittest

class TestCatMouse(unittest.TestCase):
    def test_1_2_3_in_CatMouse(self): 
        result = cat_and_mouse(1,2,3)
        self.assertEqual(result, 'Cat B')
    def test_1_3_2_in_CatMouse(self): 
        result = cat_and_mouse(1,3,2)
        self.assertEqual(result, 'Mouse C')
    def test_2_1_3_in_CatMouse(self): 
        result = cat_and_mouse(2,1,3)
        self.assertEqual(result, 'Cat A')
    def test_1_4_8_in_CatMouse(self): 
        result = cat_and_mouse(1,4,8)
        self.assertEqual(result, 'Cat B')
    def test_1_9_5_in_CatMouse(self): 
        result = cat_and_mouse(1,9,5)
        self.assertEqual(result, 'Mouse C')
