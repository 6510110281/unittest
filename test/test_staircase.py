from coe_number.Staircase import staircase

import unittest

class TestStaircase(unittest.TestCase):

    def test_give_1_to_staircase(self):
        n = 1
        pattern = '#'
        expected_output = '#'
        result = staircase(n,pattern)
        self.assertEqual(result, expected_output, f'Should be {expected_output}')

    def test_give_15_to_staircase(self):
        n = 15
        pattern = '#'
        expected_output = \
            "              #\n" + \
            "             ##\n" + \
            "            ###\n" + \
            "           ####\n" + \
            "          #####\n" + \
            "         ######\n" + \
            "        #######\n" + \
            "       ########\n" + \
            "      #########\n" + \
            "     ##########\n" + \
            "    ###########\n" + \
            "   ############\n" + \
            "  #############\n" + \
            " ##############\n" + \
            "###############\n"
            
        result = staircase(n,pattern)
        self.assertEqual(result, expected_output, f'Should be {expected_output}')

    def test_give_29_to_staircase(self):
        n = 29
        pattern = '#'
        expected_output = \
            "                            #\n" + \
            "                           ##\n" + \
            "                          ###\n" + \
            "                         ####\n" + \
            "                        #####\n" + \
            "                       ######\n" + \
            "                      #######\n" + \
            "                     ########\n" + \
            "                    #########\n" + \
            "                   ##########\n" + \
            "                  ###########\n" + \
            "                 ############\n" + \
            "                #############\n" + \
            "               ##############\n" + \
            "              ###############\n" + \
            "             ################\n" + \
            "            #################\n" + \
            "           ##################\n" + \
            "          ###################\n" + \
            "         ####################\n" + \
            "        #####################\n" + \
            "       ######################\n" + \
            "      #######################\n" + \
            "     ########################\n" + \
            "    #########################\n" + \
            "   ##########################\n" + \
            "  ###########################\n" + \
            " ############################\n" + \
            "#############################\n"

        result = staircase(n,pattern)
        self.assertEqual(result, expected_output, f'Should be {expected_output}')

    def test_give_30_to_staircase(self):
        n = 30
        pattern = '#'
        expected_output = \
            "                             #\n" + \
            "                            ##\n" + \
            "                           ###\n" + \
            "                          ####\n" + \
            "                         #####\n" + \
            "                        ######\n" + \
            "                       #######\n" + \
            "                      ########\n" + \
            "                     #########\n" + \
            "                    ##########\n" + \
            "                   ###########\n" + \
            "                  ############\n" + \
            "                 #############\n" + \
            "                ##############\n" + \
            "               ###############\n" + \
            "              ################\n" + \
            "             #################\n" + \
            "            ##################\n" + \
            "           ###################\n" + \
            "          ####################\n" + \
            "         #####################\n" + \
            "        ######################\n" + \
            "       #######################\n" + \
            "      ########################\n" + \
            "     #########################\n" + \
            "    ##########################\n" + \
            "   ###########################\n" + \
            "  ############################\n" + \
            " #############################\n" + \
            "##############################\n"

        result = staircase(n,pattern)
        self.assertEqual(result, expected_output, f'Should be {expected_output}')

    def test_give_31_to_staircase(self):
        n = 31
        pattern = '#'
        expected_output = ''
        result = staircase(n,pattern)
        self.assertEqual(result, expected_output)
        
    def test_give_0_to_staircase(self):
        n = 0
        pattern = '#'
        expected_output = ''
        result = staircase(n,pattern)
        self.assertEqual(result,expected_output)

    def test_give_negative_1_to_staircase(self):
        n = -1
        pattern = '#'
        expected_output = ''
        result = staircase(n,pattern)
        self.assertEqual(result,expected_output)