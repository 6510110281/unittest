from coe_number.GridChallenge import gridChallenge

import unittest

class TestGridChallenge(unittest.TestCase):
    def test_give_exampleList_1_to_grid(self):
        lst = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
        expected_output = 'YES'
        result = gridChallenge(lst)
        self.assertEqual(result, expected_output, f'Shoud be {expected_output}')

    def test_give_exampleList_2_to_grid(self):
        lst = ['abc', 'def', 'ghi']
        expected_output = 'YES'
        result = gridChallenge(lst)
        self.assertEqual(result, expected_output , f'Shoud be {expected_output}')

    def test_give_exampleList_3_to_grid(self):
        lst = ['cba', 'def', 'ghi']
        expected_output = 'NO'
        result = gridChallenge(lst)
        self.assertEqual(result, expected_output, f'Shoud be {expected_output}')

    def test_give_exampleList_4_to_grid(self):
        lst = ['rgb','end','dot']
        expected_output = 'NO'
        result = gridChallenge(lst)
        self.assertEqual(result, expected_output, f'Shoud be {expected_output}')

    def test_give_exampleList_5_to_grid(self):
        lst = ['abc']
        expected_output = 'YES'
        result = gridChallenge(lst)
        self.assertEqual(result, expected_output, f'Shoud be {expected_output}')
